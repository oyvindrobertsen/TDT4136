# -*- coding: utf-8 -*-

from heapq import *
import os

from grid import Grid
from draw_map import *


def find_path(grid, draw_all_steps=False, bfs=False, dijkstra=False):
    closed_nodes = list()
    start_node, goal_node = grid.startNode, grid.goalNode

    open_nodes = list()
    if bfs:
        open_nodes.append(start_node)
    else:
        heappush(open_nodes, start_node)

        # Code to generate png for each step
        # if draw_all_steps:
        # filename = "to_gif_1-1_%04d.png"
        # filename_count = 1

    while open_nodes:
        if bfs:
            node = open_nodes.pop(0)
        else:
            node = heappop(open_nodes)
        closed_nodes.append(node)

        if node == grid.goalNode:
            return get_backtrace(node), open_nodes, closed_nodes

        neighbors = grid.getNeightbors(node)

        for neighbor in neighbors:
            if neighbor in closed_nodes:
                continue

            ng = node.g + neighbor.weight

            if (neighbor not in open_nodes) or (neighbor.g and ng < neighbor.g):
                neighbor.g = ng

                neighbor.h = 0 if dijkstra else grid.h(neighbor, goal_node)
                neighbor.parent = node

                if neighbor not in open_nodes:
                    if bfs:
                        open_nodes.append(neighbor)
                    else:
                        heappush(open_nodes, neighbor)


def get_backtrace(node):
    nodes = []
    while node.parent:
        nodes.append(node)
        node = node.parent
    return nodes[1:]


def print_map(grid, path):
    print filepath
    matrix = [row[:] for row in grid.matrix]
    for node in path:
        matrix[node.x][node.y] = "O"

    for row in matrix:
        print "".join(row)
    print


if __name__ == "__main__":
    dir_name = os.getcwd()
    for filename in os.listdir(os.path.join(dir_name, 'boards')):

        # Create a Grid object en
        filepath = dir_name + '/boards/' + filename
        grid = Grid(filepath)

        # Find path with additional info
        bfs = False
        dijkstra = False
        path, open_list, closed_list = find_path(grid, bfs=bfs, dijkstra=dijkstra)

        # Print the map including best path to console
#        print_map(grid, path)

        # Draw the board to png-file, requires PIL.
        if bfs:
            what = 'bfs'
        elif dijkstra:
            what = 'dijkstra'
        else:
            what = 'astar'


        new_file = os.path.join(dir_name, "pictures", filename.replace('.txt', '-{}.png'.format(what)))

        draw_map(grid, new_file, path, open_list, closed_list)
