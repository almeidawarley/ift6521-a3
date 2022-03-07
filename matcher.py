import random as rd

class Matcher:

    def __init__(self, problem, analytical, backward, evaluations, seed = 100):

        # Store instance object
        self.instance = problem
        
        # Store solver classes
        self.analytical_class = analytical
        self.backward_class = backward

        # Store number of evaluations
        self.evaluation_number = evaluations
        
        # Set seed accordingly
        rd.seed(seed)

    def build(self):

        print('Building the matcher between analytical and backward solvers')

        # Build analytical solver and compute optimal analytical policy
        self.analytical_solver = self.analytical_class(self.instance)
        self.analytical_policy = self.analytical_solver.run()

        # Build backward solver and compute optimal backward policy
        self.backward_solver = self.backward_class(self.instance)
        self.backward_policy = self.backward_solver.run()

    def run(self):
      
        print('Comparing analytical and backward optimal policies ({} evaluations)'.format(self.evaluation_number))

        # Draw random k and x to compare optimal policy
        evaluation_counter = 1
        while evaluation_counter <= self.evaluation_number:
            k = rd.choice(range(0, self.instance.N))
            x = rd.choice(range(- self.instance.peak, self.instance.peak + 1))
            self.log(k, x)
            evaluation_counter = evaluation_counter + 1

    def log(self, k, x):

        # Retrieve optimal analytical policy
        a = self.analytical_policy(k, x)

        # Retrieve optimal backward policy
        b = self.backward_policy(k, x)

        print('\t{} :: Analytical \mu*_{}({}) = {} units - Backward \mu*_{}({}) = {} units'.format('They are EQUAL' if a == b else 'They are DIFFERENT', k, x, a, k, x, b))