from node import Node

WEIGHTS = {
    'w': 100,
    'm': 50,
    'f': 10,
    'g': 5,
    'r': 1,
    '#': 1,
    '.': 1,
    'A': 0,
    'B': 0,
}

get_weight = lambda x: WEIGHTS[x]


class Grid(object):
    def __init__(self, file_path):
        try:
            open_file = open(file_path)
        except IOError:
            print 'File not found'

        self.lines = [[c for c in line.strip()] for line in open_file.readlines() if not line.isspace()]
        self.node_weights = [list(map(get_weight, row)) for row in self.lines]
        self.height, self.width = len(self.lines), len(self.lines[0])

        nodes = [[Node(i, j) for j in range(self.width)] for i in range(self.height)]

        for i, row in enumerate(nodes):
            for j, node in enumerate(row):

                node.walkable = False if self.lines[i][j] == "#" else True
                node.weight = self.node_weights[i][j]

                # Set start and goal node
                if self.lines[i][j] == "A":
                    self.start_node = node
                    self.start_node.g = 0
                elif self.lines[i][j] == "B":
                    self.end_node = node

        self.nodes = nodes

    def is_walkable_at(self, x, y):
        return self.is_within_bounds(x, y) and self.nodes[x][y].walkable

    def is_within_bounds(self, x, y):
        return x in range(self.height) and y in range(self.width)

    def get_adjacent_nodes(self, node):
        x = node.x
        y = node.y
        adjacent_nodes = []

        if self.is_walkable_at(x, y - 1):
            adjacent_nodes.append(self.nodes[x][y - 1])

        if self.is_walkable_at(x, y + 1):
            adjacent_nodes.append(self.nodes[x][y + 1])

        if self.is_walkable_at(x - 1, y):
            adjacent_nodes.append(self.nodes[x - 1][y])

        if self.is_walkable_at(x + 1, y):
            adjacent_nodes.append(self.nodes[x + 1][y])

        return adjacent_nodes

    @staticmethod
    def manhattan_distance(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

