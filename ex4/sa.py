from __future__ import division
from math import exp
from random import random, choice


class SimAnnealer(object):
    '''
    An implementation of the Simulated Annealing algorithm.
    '''

    def __init__(self, t_max, delta_t, num_neighbors, f_target):
        self.t_max = t_max
        self.delta_t = delta_t
        self.num_neighbors = num_neighbors
        self.f_target = f_target

    def search(self, start):
        'Perform the actual annealing, starting from the solution node passed.'
        try:
            p = start
            t = self.t_max
            while t > 0:
                # Evaluate the current solution node
                fitness = p.obj_func()
                # Is it good enough?
                if fitness >= self.f_target:
                    return p
                # It is not, generate some neighbors
                neighbors = p.gen_neighbors(self.num_neighbors)
                # Find the best neighbor
                p_max = max(neighbors, key=(lambda n: n.obj_func()))
                # Calculate exploiting/exploring threshold
                q = (p_max.obj_func() - fitness) / fitness
                f = exp(-q / t)
                p_val = min(1, f)
                x = random()
                if x > p_val:
                    # Exploit
                    p = p_max
                else:
                    # Explore
                    p = choice(neighbors)
                # Decrease temperature by delta_t to restrict the process.
                t = t - self.delta_t
            print('No solution with p.obj_func() > f_target was found, ' +
                  'return last examined board.')
            return p
        except KeyboardInterrupt:
            print("KeyboardInterrupt, last p was:")
            print(p)
            exit(0)
