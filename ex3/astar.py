# -*- coding: utf-8 -*-

from heapq import *
import os

from grid import Grid
from draw_map import *


def find_path(grid, algorithm='astar'):
    closed_nodes = list()

    open_nodes = list()
    if algorithm == 'bfs':
        open_nodes.append(grid.start_node)
    else:
        heappush(open_nodes, grid.start_node)

    while open_nodes:
        current_node = open_nodes.pop(0) if algorithm == 'bfs' else heappop(open_nodes)
        closed_nodes.append(current_node)

        if current_node == grid.end_node:
            return backtrack(current_node), open_nodes, closed_nodes

        adjacent_nodes = grid.get_adjacent_nodes(current_node)

        for adjacent_node in adjacent_nodes:
            if adjacent_node in closed_nodes:
                continue

            new_g = current_node.g + adjacent_node.weight

            if (adjacent_node not in open_nodes) or (adjacent_node.g and new_g < adjacent_node.g):
                adjacent_node.g = new_g

                adjacent_node.h = 0 if algorithm == 'dijkstra' else grid.manhattan_distance(adjacent_node, grid.end_node)
                adjacent_node.parent = current_node

                if adjacent_node not in open_nodes:
                    if algorithm == 'bfs':
                        open_nodes.append(adjacent_node)
                    else:
                        heappush(open_nodes, adjacent_node)


def backtrack(node):
    nodes = []
    while node.parent:
        nodes.append(node)
        node = node.parent
    return nodes[1:]


def print_map(map, path):
    print file_path
    grid = [row[:] for row in map.lines]
    for node in path:
        grid[node.x][node.y] = "O"

    for row in grid:
        print "".join(row)
    print


if __name__ == "__main__":
    dir_name = os.getcwd()
    for filename in os.listdir(os.path.join(dir_name, 'boards')):
        for algorithm in ['astar', 'dijkstra', 'bfs']:
            # Create a Grid object en
            file_path = os.path.join(dir_name, 'boards', filename)
            grid = Grid(file_path)

            # Find path with additional info
            path, open_list, closed_list = find_path(grid, algorithm=algorithm)

            # Print the map including best path to console
            # print_map(grid, path)

            # Draw the board to png-file, requires PIL.
            new_file = os.path.join(dir_name, "pictures", filename.replace('.txt', '-{}.png'.format(algorithm)))

            draw_map(grid, new_file, path, open_list, closed_list)
