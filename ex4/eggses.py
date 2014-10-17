from __future__ import division
from random import randrange
from copy import deepcopy
from time import process_time

from numpy.lib.twodim_base import flipud
from numpy.ma.core import array

from sa import SimAnnealer


# static helper functions
def grid_dimensions(grid):
    return len(grid[0]), len(grid)


def random_coordinate(M, N):
    return randrange(M), randrange(N)


def new_grid(width, height, initial_value=0):
    return [[initial_value for _ in range(width)] for _ in range(height)]


def random_grid(width, height, ones):
    grid = new_grid(width, height, 0)
    ts = ones * min(width, height)
    while ts > 0:
        x, y = random_coordinate(width, height)

        if grid[y][x] == 1:
            continue

        grid[y][x] = 1
        ts -= 1

    return grid


def grid_score(k, grid):
    width, height = grid_dimensions(grid)

    row_penalties = list(max(0, sum(row) - k) for row in grid)
    col_penalties = list(max(0, sum(row[j] for row in grid) - k) for j in range(width))

    grid = array(grid)
    flip = flipud(grid)

    r1 = range(-(width - 1), width)
    r2 = range(-(height - 1), height)

    dia_penalties = lambda m, dia_i: max(0, int(m.trace(dia_i)) - k)

    di1_penalties = list(dia_penalties(grid, d) for d in r1)
    di2_penalties = list(dia_penalties(flip, d) for d in r2)

    return sum(row_penalties) + sum(col_penalties) + sum(di1_penalties) + sum(di2_penalties)


def random_swap(grid):
    width, height = grid_dimensions(grid)

    x1, y1 = random_coordinate(width, height)
    x2, y2 = random_coordinate(width, height)

    while (x1 == x2 and y1 == y2) or grid[y1][x1] == grid[y2][x2]:
        x2, y2 = random_coordinate(width, height)

    grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]

    return grid


class Carton:
    def __init__(self, k, grid):
        self.grid = deepcopy(grid)
        self.k = k
        self.width, self.height = grid_dimensions(self.grid)

    @property
    def worst_score(self):
        one_grid = new_grid(self.width, self.height, 1)
        return grid_score(self.k, one_grid)

    def gen_neighbors(self, n):
        ret = []
        while len(ret) < n:
            new = Carton(self.k, self.grid)
            random_swap(new.grid)
            if new not in ret:
                ret.append(new)

        return ret

    def obj_func(self):
        return 1 - (grid_score(self.k, self.grid) / self.worst_score)

    def __str__(self):
        '''
        Display grid state with row and column sums
        '''
        r = ""
        for j in range(self.height):
            r += ' '.join("O" if x else "." for x in self.grid[j])
            r += ' | {}'.format(sum(self.grid[j]))
            r += '\n'
        r += ' '.join('-' for j in range(self.width))
        r += '\n'
        r += ' '.join(str(sum(row[j] for row in self.grid)) for j in range(self.width))
        r += '\n'
        r += "Score: {}".format(str(self.obj_func()))
        return r


# obj_func test cases
SOLUTION_552 = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 0]]
assert Carton(2, SOLUTION_552).obj_func() == 1.0

ONES = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
assert Carton(2, ONES).obj_func() == 0.0


# use SA for egg probmles of different M, N, K
CASES = (
    (5, 5, 2),
    (6, 6, 2),
    (8, 8, 1),
    (10, 10, 3),
)
annealer = SimAnnealer(1, 0.001, 5, 0.98)
for M, N, K in CASES:
    print(' '.join('#' for _ in range(10)))
    # print("M, N, K = {}, {}, {}".format(M, N, K))
    # print()

    carton = Carton(K, random_grid(M, N, K))
    print(carton)
    print()
    start = process_time()
    annealer.search(carton)
    end = process_time()
    # print("Time: {}".format(end - start))
