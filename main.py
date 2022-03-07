import instance as it
import analytical as an
import backward as bc
import argparse as ag
import matcher as mt

# Parse command line arguments
parser = ag.ArgumentParser(description = 'Compute analytical form and backward chaining optimal policies for an inventory problem instance')
parser.add_argument('path', type = str, help = 'Path to the text file with the instance information')
parser.add_argument('--evaluations', type = int, help = 'Number of sampled states to evaluate the optimal policy', default = 10)
arguments = parser.parse_args()

# Read instance information from a text file
problem = it.Instance(arguments.path)

# Create an evaluator with the solvers
evaluator = mt.Matcher(problem, an.Analytical, bc.Backward, arguments.evaluations)

# Build evaluator and run it
evaluator.build()
evaluator.run()