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

manhattan_distance = lambda a, b: abs(a.x - b.x) + abs(a.y - b.y)


class Grid(object):
    def __init__(self, file_path):
        try:
            open_file = open(file_path)
        except IOError:
            print "Could not open {}".format(file_path)

        self.lines = [[c for c in line.strip()] for line in open_file.readlines() if not line.isspace()]
        self.node_weights = [list(map(get_weight, row)) for row in self.lines]
        self.height, self.width = len(self.lines), len(self.lines[0])

        nodes = [[Node(i, j) for j in range(self.width)] for i in range(self.height)]

        for i, row in enumerate(nodes):
            for j, node in enumerate(row):
                node.open = False if self.lines[i][j] == "#" else True
                node.weight = self.node_weights[i][j]

                if self.lines[i][j] == "A":
                    self.start_node = node
                    self.start_node.g = 0
                elif self.lines[i][j] == "B":
                    self.end_node = node

        self.nodes = nodes

    def is_within_bounds(self, x, y):
        return x in range(self.height) and y in range(self.width)

    def is_open_at(self, x, y):
        return self.is_within_bounds(x, y) and self.nodes[x][y].open

    def get_adjacent_nodes(self, node):
        candidates = [(node.x + a, node.y + b) for b in range(-1, 2) for a in range(-1, 2) if abs(a) != abs(b)]
        return [self.nodes[n[0]][n[1]] for n in candidates if self.is_open_at(*n)]