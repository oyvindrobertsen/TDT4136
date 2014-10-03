# -*- coding: utf-8 -*-

from heapq import *
import os

from grid import Grid, manhattan_distance
from draw_map import *
from node import push_node, pop_node

ALGORITHMS = ['astar', 'dijkstra', 'bfs']


def find_path(grid, algorithm='astar'):
    use_heap_methods = (algorithm != 'bfs')

    closed_nodes, open_nodes = list(), list()

    push_node(open_nodes, grid.start_node)

    while open_nodes:
        current_node = pop_node(open_nodes, heap=use_heap_methods)
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

                adjacent_node.h = 0 if algorithm == 'dijkstra' else manhattan_distance(adjacent_node, grid.end_node)
                adjacent_node.parent = current_node

                if adjacent_node not in open_nodes:
                    push_node(open_nodes, adjacent_node, heap=use_heap_methods)


def backtrack(node):
    nodes = []
    while node.parent:
        nodes.append(node)
        node = node.parent
    return nodes


def print_map(map, path):
    grid = [row[:] for row in map.lines]
    for node in path:
        grid[node.x][node.y] = "O"

    for row in grid:
        print "".join(row)
    print


if __name__ == "__main__":
    dir_name = os.getcwd()
    for filename in os.listdir(os.path.join(dir_name, 'boards')):
        for algorithm in ALGORITHMS:
            grid = Grid(os.path.join(dir_name, 'boards', filename))

            image_name = filename.replace('.txt', '-{}.png'.format(algorithm))
            image_path = os.path.join(dir_name, "pictures", image_name)

            draw_map(grid, image_path, *find_path(grid, algorithm))
