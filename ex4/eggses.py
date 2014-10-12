from numpy.lib.twodim_base import flipud
from numpy.ma.core import array
from random import choice
from copy import deepcopy
from sa import SimAnnealer

SOLUTION552 = [[1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1],
               [0, 1, 0, 1, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 1, 1, 0]]

ONES = [[1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]

MNKs = [(5, 5, 2),
        (6, 6, 2),
        (8, 8, 1),
        (10, 10, 3)]


class Carton:

    def __init__(self, k, grid):
        self.grid = deepcopy(grid)
        self.k = k
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def gen_neighbors(self, n):
        ret = []
        while len(ret) < n:
            new = self.gen_neighbor()
            if new not in ret:
                ret.append(new)
        return ret

    def gen_neighbor(self):
        ret = Carton(self.k, self.grid)
        rnd_x = choice(range(self.width))
        rnd_y = choice(range(self.height))
        ret.grid[rnd_y][rnd_x] = int(not ret.grid[rnd_y][rnd_x])
        return ret

    def obj_func(self):
        row_d = abs(sum(map(lambda l: sum(l) - self.k, self.grid)))
        col_d = abs(sum(sum(row[j] for row in self.grid) - self.k for j in range(self.width)))

        grid = array(self.grid)
        flip = flipud(grid)
        di1_d = abs(sum((grid.trace(d) - min(self.k, len(grid.diagonal(d))) for d in range(-(self.width - 1), self.width))))
        di2_d = abs(sum((flip.trace(d) - min(self.k, len(flip.diagonal(d))) for d in range(-(self.height - 1), self.height))))

        perf = self.k * (self.height + self.width + 2 * (self.width + self.height - 1))
        return (perf - row_d - col_d - di1_d - di2_d) / perf

    def __str__(self):
        ret = ""
        for j in range(self.height):
            ret += str(self.grid[j])
            ret += '\n'
        ret += str(self.obj_func())
        ret += '\n'
        return ret


annealer = SimAnnealer(10, 0.2, 5, 0.75)
print(annealer.search(Carton(2, ONES)))
