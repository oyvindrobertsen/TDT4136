from math import exp
from random import random, choice


class SimAnnealer(object):

    def __init__(self, t_max, delta_t, num_neighbors, f_target):
        self.t_max = t_max
        self.delta_t = delta_t
        self.num_neighbors = num_neighbors
        self.f_target = f_target

    def search(self, start):
        p = start
        t = self.t_max
        while p:
            fitness = p.obj_func()
            if fitness >= self.f_target:
                return p
            neighbors = p.gen_neighbors(self.num_neighbors)
            neighbor_fitness = {neighbor: neighbor.obj_func() for neighbor
                                in neighbors}
            p_max = max(neighbor_fitness.iterkeys(), key=(lambda key:
                        neighbor_fitness[key]))
            q = (neighbor_fitness[p_max] - fitness) / fitness
            p = min(1, exp(-q / t))
            x = random()
            if x > p:
                p = p_max
            else:
                p = choice(neighbors)
            t = t - self.delta_t
