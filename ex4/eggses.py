from numpy.lib.twodim_base import flipud
from numpy.ma.core import array

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


def eggs_obj(grid, K):
    M = len(grid)
    N = len(grid[0])

    row_d = abs(sum(map(lambda l: sum(l) - K, grid)))
    col_d = abs(sum(sum(row[j] for row in grid) - K for j in range(N)))

    grid = array(grid)
    flip = flipud(grid)
    di1_d = abs(sum((grid.trace(d) - min(K, len(grid.diagonal(d))) for d in range(-(N - 1), N))))
    di2_d = abs(sum((flip.trace(d) - min(K, len(flip.diagonal(d))) for d in range(-(M - 1), M))))

    perf = K * (M + N + 2 * (N + M - 1))
    return (perf - row_d - col_d - di1_d - di2_d)/perf


print(eggs_obj(ONES, 2))