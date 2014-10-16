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
            best_p = p
            t = self.t_max
            while p:
                fitness = p.obj_func()
                if fitness >= self.f_target:
                    return p
                neighbors = p.gen_neighbors(self.num_neighbors)
                p_max = max(neighbors, key=(lambda n: n.obj_func()))

                if p_max.obj_func() > best_p.obj_func():
                    best_p = p_max
                    # print(best_p)

                q = (p_max.obj_func() - fitness) / fitness
                f = exp(-q / t)
                p = min(1, f)
                x = random()
                if x > p:
                    p = p_max
                else:
                    p = choice(neighbors)
                t = t - self.delta_t
        except KeyboardInterrupt:
            print("KeyboardInterrupt, best p is:")
            print(best_p)
            exit(0)