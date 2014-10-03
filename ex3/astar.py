# -*- coding: utf-8 -*-

from heapq import *
from grid import Grid
from draw_map import *
import os


def find_path(grid, draw_all_steps=False, bfs=False, dijkstra=False):
    closed_list = []
    startNode = grid.startNode
    goalNode = grid.goalNode

    open_list = []
    if bfs:
        open_list.append(startNode)
    else:
        heappush(open_list, startNode)

    while(open_list):
        if bfs:
            node = open_list.pop(0)
        else:
            node = heappop(open_list)
        closed_list.append(node)

        if (node == grid.goalNode):
            best_path = get_backtrace(node)
            return best_path, open_list, closed_list

        neightbors = grid.getNeightbors(node)

        for neighbor in neightbors:
            if neighbor in closed_list:
                continue

            ng = node.g + neighbor.weight

            if (neighbor not in open_list) or (neighbor.g and ng < neighbor.g):
                neighbor.g = ng

                if dijkstra:
                    neighbor.h = 0
                else:
                    neighbor.h = grid.h(neighbor, goalNode)
                neighbor.parent = node

                if neighbor not in open_list:
                    if bfs:
                        open_list.append(neighbor)
                    else:
                        heappush(open_list, neighbor)


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
        print("".join(row))
    print


if __name__ == "__main__":
    dir_name = os.getcwd()
    for filename in os.listdir(os.path.join(dir_name + '/boards/')):

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
            new_file = dir_name + "/pictures/" + filename.replace('.txt', '-bfs.png')
        elif dijkstra:
            new_file = dir_name + "/pictures/" + filename.replace('.txt', '-dijkstra.png')
        else:
            new_file = dir_name + "/pictures/" + filename.replace('.txt', '.png')

        draw_map(grid, new_file, path, open_list, closed_list)
