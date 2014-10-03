# -*- coding: utf-8 -*-
from math import sqrt

from node import push_node, pop_node

ALGORITHMS = ['astar', 'dijkstra', 'bfs']

manhattan_distance = lambda a, b: abs(a.x - b.x) + abs(a.y - b.y)
euclidean = lambda a, b: sqrt(abs(a.x - b.x) ** 2 + abs(a.y - b.y) ** 2)


def find_path(grid, algorithm='astar', heuristic=manhattan_distance):
    '''
    :param grid: initialized Grid object
    :param algorithm: text string, one of the options in ALGORITHMS
    :param heuristic: manhattan_distance or euclidean
    :return: tuple of (1) list of nodes in the path from grid.start_node to grid.end_node
                      (2) list of remaining open nodes
                      (3) list of closed nodes
    '''
    use_heap_methods = (algorithm != 'bfs')

    closed_nodes, open_nodes = list(), list()

    push_node(open_nodes, grid.start_node)

    while open_nodes:
        current_node = pop_node(open_nodes, heap=use_heap_methods)
        closed_nodes.append(current_node)

        if current_node == grid.end_node:
            return backtrack(current_node), open_nodes, closed_nodes

        adjacent_nodes = grid.get_adjacent_nodes(current_node, allow_diagonal=False)

        for adjacent_node in adjacent_nodes:
            if adjacent_node in closed_nodes:
                continue

            new_g = current_node.g + adjacent_node.weight

            if (adjacent_node not in open_nodes) or (adjacent_node.g and new_g < adjacent_node.g):
                adjacent_node.g = new_g

                adjacent_node.h = 0 if algorithm == 'dijkstra' else heuristic(adjacent_node, grid.end_node)
                adjacent_node.parent = current_node

                if adjacent_node not in open_nodes:
                    push_node(open_nodes, adjacent_node, heap=use_heap_methods)


def backtrack(node, path=None):
    if path is None:
        path = []

    path.append(node)

    if node.parent is None:
        return path[::-1]

    return backtrack(node.parent, path)
