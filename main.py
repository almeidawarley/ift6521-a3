import instance as it
import analytical as an
import backward as bc
import argparse as ag
import matcher as mt

# Parse command line arguments
parser = ag.ArgumentParser(description = 'Compute analytical form and backward chaining optimal policies for an inventory problem instance')
parser.add_argument('path', type = str, help = 'Path to the text file with the instance information')
parser.add_argument('--modified', action = 'store_true', help = 'Work with the modified problem with piecewise ordering costs', default = False)
parser.add_argument('--validate', action = 'store_true', help = 'Validate analytical and backward solvers with values computed by hand', default = False)
arguments = parser.parse_args()

# Read instance information from a text file
problem = it.Instance(arguments.path, arguments.modified)

# Create an evaluator with the solvers
evaluator = mt.Matcher(problem, an.Analytical, bc.Backward)

# Build evaluator and run it
evaluator.build()
evaluator.run()

# Validate computations
if arguments.validate:
    evaluator.validate()