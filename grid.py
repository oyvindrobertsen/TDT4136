from node import Node

class Grid(object):

    def __init__(self, filepath):
        self._build_matrix(filepath)
        self._build_nodes()

    def _build_matrix(self, filepath):
        self.matrix = self._read_map(filepath)
        self.weighted_matrix = self._get_weighted_matrix(self.matrix)
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def _read_map(self, path):
        try:
            f = open(path)
        except IOError:
            print('File not found')
        else:
            return self._parseMap(f)

    def _parseMap(self, file):
        grid = []
        for line in file.readlines():
            if not line.isspace():
                grid.append([c for c in line.strip()])
        return grid

    def _get_weighted_matrix(self, matrix):
        weighted_matrix = []
        for row in matrix:
            weighted_matrix.append(list(map(self._get_weights, row)))
        return weighted_matrix

    def _get_weights(self, letter):
        weights = {'r': 1, 'g': 5, 'f': 10, 'm': 50, 'w': 100,
            'A': 0, 'B': 0, '.': 1, '#': 1}
        return weights[letter]

    def _build_nodes(self):
        nodes = [[Node(i, j) for j in range(self.width)] for i in range(self.height)]

        for i, row in enumerate(nodes):
            for j, node in enumerate(row):

                node.walkable = False if self.matrix[i][j] == "#" else True
                node.weight = self.weighted_matrix[i][j]

                # Set start and goal node
                if self.matrix[i][j] == "A":
                    self.startNode = node
                    self.startNode.g = 0
                elif self.matrix[i][j] == "B":
                    self.goalNode = node

        self.nodes = nodes

    def isWalkableAt(self, x, y):
        return self.isInside(x, y) and self.nodes[x][y].walkable

    def isInside(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width

    def getNeightbors(self, node):
        x = node.x
        y = node.y
        neightbors = []

        if self.isWalkableAt(x, y-1):
            neightbors.append(self.nodes[x][y-1])

        if self.isWalkableAt(x, y+1):
            neightbors.append(self.nodes[x][y+1])

        if self.isWalkableAt(x-1, y):
            neightbors.append(self.nodes[x-1][y])

        if self.isWalkableAt(x+1, y):
            neightbors.append(self.nodes[x+1][y])

        return neightbors

    def h(self, node, goalNode):
        dx = abs(node.x - goalNode.x)
        dy = abs(node.y - goalNode.y)
        return (dx + dy)

