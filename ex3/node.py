from _heapq import heappush, heappop


def push_node(data_structure, node, heap=False):
    if heap:
        heappush(data_structure, node)
    else:
        data_structure.append(node)


def pop_node(data_structure, heap=False):
    return heappop(data_structure) if heap else data_structure.pop(0)


class Node(object):
    def __init__(self, x, y, open=None):
        self.x = x
        self.y = y
        self.open = open if (open is not None) else True
        self.g = None
        self.h = None
        self.parent = None
        self.type = None
        self.weight = None

    def __lt__(self, other):
        if self.f() == other.f():
            return self.h < other.h

        return self.f() < other.f()

    def f(self):
        return self.g + self.h

    def __str__(self):
        return "{}:{}".join(str(self.x), str(self.y))
