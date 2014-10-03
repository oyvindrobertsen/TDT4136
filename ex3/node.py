from _heapq import heappush, heappop


def push_node(data_structure, node, heap=False):
    if heap:
        heappush(data_structure, node)
    else:
        data_structure.append(node)


def pop_node(data_structure, heap=False):
    return heappop(data_structure) if heap else data_structure.pop(0)


class Node(object):
    '''
    Holds data for the individual tiles of the board.
    pathfinding.py can set g, h and parent during board processing.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = None
        self.h = None
        self.parent = None
        self.weight = None

    def __lt__(self, other):
        if self.f == other.f:
            return self.h < other.h

        return self.f < other.f

    @property
    def f(self):
        return self.g + self.h

    @property
    def is_wall(self):
        return self.weight == -1

    def __str__(self):
        return "{}:{}".join(str(self.x), str(self.y))
