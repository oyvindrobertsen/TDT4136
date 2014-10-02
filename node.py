

class Node(object):

    def __init__(self, x, y, walkable=None):
        self.x = x
        self.y = y
        self.walkable = walkable if walkable else True
        self.g = None
        self.h = None
        self.parent = None

        self.type = None
        self.weight = None

    def __lt__(self, other):
        return self.f() < other.f()

    def f(self):
        return self.g + self.h

    def __str__(self):
        return str(self.x) + ":" + str(self.y)