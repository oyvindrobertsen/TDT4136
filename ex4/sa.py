from math import exp
from random import random, choice


class SimAnnealer(object):

    def __init__(self, p_start, t_max, delta_t, obj_func, gen_neighbors,
                 num_neighbors, f_target):
        self.p_start = p_start
        self.t_max = t_max
        self.delta_t = delta_t
        self.obj_func = obj_func
        self.gen_neighbors = gen_neighbors
        self.num_neighbors = num_neighbors
        self.f_target = f_target

    def search(self, start):
        p = start
        t = self.t_max
        while p:
            fitness = self.obj_func(p)
            if fitness >= self.f_target:
                return p
            neighbors = self.gen_neighbors(self.num_neighbors)
            neighbor_fitness = {neighbor: self.obj_func(neighbor) for neighbor
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
