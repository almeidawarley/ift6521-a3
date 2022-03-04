import instance as it
import analytical as an
import backward as bc
import random as rd
import argparse as ag

rd.seed(50)

def log_policy(policy1, policy2, stages, states):

    for k in stages:

        print('> Stage {}:'.format(k))

        for x in states:

            print('\tOptimal {} policy for inventory {} \mu*_{}({}) = {} units'.format('analytical', x, k, x, policy1(k, x)))
            print('\tOptimal {} policy for inventory {} \mu*_{}({}) = {} units'.format('backwards', x, k, x, policy2(k, x)))

# Parse command line arguments
parser = ag.ArgumentParser(description = 'Compute analytical form and backward chaining optimal policies for an inventory problem instance')
parser.add_argument('path', type = str, help = 'Path to the text file with the instance information')
parser.add_argument('--states', type = int, help = 'Number of sampled states to evaluate the optimal policy', default = 10)
arguments = parser.parse_args()

# Read instance information from a text file
problem = it.Instance(arguments.path)

# Create list of stages from the problem instance
stages = list(range(0, problem.N))

# Sample states to evaluate the optimal policy
counter = 0
states = []
while counter <= arguments.states:
    state = rd.randint(-1 * problem.peak, problem.peak)
    states.append(state)
    counter = counter + 1
states = sorted(states)

# Create the analytical form solver
solver = an.Analytical(problem)

# Compute the optimal policy 
policy1 = solver.run()

# Create the backward chaining solver
solver = bc.Backward(problem)

# Compute the optimal policy
policy2 = solver.run()

log_policy(policy1, policy2, stages, states)

print(problem)