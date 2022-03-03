from inspect import BoundArguments
import instance as it
import analytical as an
import backward as bc
import random as rd

sim_number = 5

problem = it.Instance('small.txt')

solver1 = an.Analytical(problem)
solver2 = bc.Backward(problem)

policy1 = solver1.run()
policy2 = solver2.run()

for k in range(0, problem.N):

    for x in range(-problem.peak, problem.peak):
        print('# Stage {}, state {}'.format(k, x))
        print('\tOptimal (analytical) policy for an inventory at level {} in stage {} -> order {} units'.format(x, k, policy1(k, x)))
        print('\tOptimal (backward) policy for an inventory at level {} in stage {} -> order {} units'.format(x, k, policy2(k, x)))

        _ = input('Press enter to move forward...')