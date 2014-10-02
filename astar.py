# -*- coding: utf-8 -*-

from heapq import *
from grid import Grid
from draw_map import *
import os

def find_path(grid, draw_all_steps=False):
    open_list = []
    closed_list = []

    startNode = grid.startNode
    heappush(open_list, startNode)
    
    goalNode = grid.goalNode

    # Code to generate png for each step
    # filename = "to_gif_1-1_%04d.png"
    # filename_count = 1

    while(open_list):
        node = heappop(open_list)
        closed_list.append(node)

        # Code to generate png for each step
        # draw_map(grid, filename % filename_count, None, open_list, closed_list)
        # filename_count += 1

        if (node == grid.goalNode):
            best_path = get_backtrace(node)
            return best_path, open_list, closed_list

        neightbors = grid.getNeightbors(node)

        for neighbor in neightbors:
            if neighbor in closed_list:
                continue

            x = neighbor.x
            y = neighbor.y

            ng = node.g + neighbor.weight

            if (neighbor not in open_list) or (neighbor.g and ng < neighbor.g):
                neighbor.g = ng
                neighbor.h = grid.h(neighbor, goalNode)
                neighbor.parent = node

                if neighbor not in open_list:
                    heappush(open_list, neighbor)


def get_backtrace(node):
    nodes = []
    while node.parent:
        nodes.append(node)
        node = node.parent
    return nodes[1:]

def print_map(grid, path):
    print filepath
    matrix = y = [row[:] for row in grid.matrix]
    for node in path:
        matrix[node.x][node.y] = "O"

    for row in matrix:
        print("".join(row))
    print


if __name__ == "__main__":
    dir_name = os.getcwd()
    for filename in os.listdir(os.path.join(dir_name + '/boards/')):

        # Initiate grid
        filepath = dir_name + '/boards/' + filename
        grid = Grid(filepath)

        # Find path with additional info
        path, open_list, closed_list = find_path(grid)

        print_map(grid, path)

        # Draw the board to png-file, requires PIL. Comment
        new_file = dir_name + "/pictures/" + filename.replace('.txt', '.png')
        draw_map(grid, new_file, path, open_list, closed_list)


