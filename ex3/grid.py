from node import Node

WEIGHTS = {
    'w': 100,
    'm': 50,
    'f': 10,
    'g': 5,
    'r': 1,
    '.': 1,
    'A': 0,
    'B': 0,
    '#': -1,
}

get_weight = lambda x: WEIGHTS[x]


class Grid(object):
    '''
    Holds all the map data which is used by pathfinding.py.
    Initalize with a .txt board.
    '''

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
                node.weight = self.node_weights[i][j]

                if self.lines[i][j] == "A":
                    self.start_node = node
                    self.start_node.g = 0
                elif self.lines[i][j] == "B":
                    self.end_node = node

        self.nodes = nodes

    def is_within_bounds(self, x, y):
        return x in range(self.height) and y in range(self.width)

    def get_adjacent_nodes(self, node, allow_diagonal=False):
        adjacent_nodes = [self.nodes[node.x + a][node.y + b]
                          for b in range(-1, 2)
                          for a in range(-1, 2)
                          if (allow_diagonal or abs(a) != abs(b))
                          and self.is_within_bounds(node.x + a, node.y + b)]
        return [n for n in adjacent_nodes if not n.is_wall]