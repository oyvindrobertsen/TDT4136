from __future__ import division
from math import exp
from random import random, choice


class SimAnnealer(object):
    def __init__(self, t_max, delta_t, num_neighbors, f_target):
        self.t_max = t_max
        self.delta_t = delta_t
        self.num_neighbors = num_neighbors
        self.f_target = f_target

    def search(self, start):
        try:
            p = start
            t = self.t_max
            while t > 0:
                fitness = p.obj_func()
                if fitness >= self.f_target:
                    return p
                neighbors = p.gen_neighbors(self.num_neighbors)
                p_max = max(neighbors, key=(lambda n: n.obj_func()))
                q = (p_max.obj_func() - fitness) / fitness
                f = exp(-q / t)
                p_val = min(1, f)
                x = random()
                if x > p_val:
                    p = p_max
                else:
                    p = choice(neighbors)
                t = t - self.delta_t
            print('No solution with p.obj_func() > f_target was found, last' +
                  'solution examined was.')
            return p
        except KeyboardInterrupt:
            print("KeyboardInterrupt, last p was:")
            print(p)
            exit(0)
