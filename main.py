from inspect import BoundArguments
import instance as it
import analytical as an
import random as rd

bound = 100
sim_number = 10

problem = it.Instance('small.txt')

solver = an.Analytical(problem)

policy = solver.run()

for k in range(0, problem.N):

    sim_counter = 1
    while sim_counter <= sim_number:
        x = rd.randint(-1 * bound, bound)
        print('Optimal policy for an inventory at level {} in stage {} -> order {} units'.format(x, k, policy(k, x)))
        sim_counter = sim_counter + 1