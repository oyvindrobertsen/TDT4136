import os

from graphics import draw_map
from grid import Grid
from pathfinding import find_path


ALGORITHMS = ['astar', 'dijkstra', 'bfs']
if __name__ == "__main__":
    dir_name = os.getcwd()
    for filename in os.listdir(os.path.join(dir_name, 'boards')):
        for algorithm in ALGORITHMS:
            grid = Grid(os.path.join(dir_name, 'boards', filename))

            image_name = filename.replace('.txt', '-{}.png'.format(algorithm))
            image_path = os.path.join(dir_name, "report", "img", image_name)

            draw_map(grid, image_path, *find_path(grid, algorithm))
            print "Wrote {}".format(image_name)