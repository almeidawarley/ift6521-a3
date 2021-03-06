import matplotlib.pyplot as plt

class Matcher:

    def __init__(self, problem, analytical, backward):

        # Store instance object
        self.instance = problem
        
        # Store solver classes
        self.analytical_class = analytical
        self.backward_class = backward

    def build(self):

        print('Building the matcher between analytical and backward solvers')

        print('\tCreating and running the analytical solver')

        # Build analytical solver and compute optimal analytical policy
        self.analytical_solver = self.analytical_class(self.instance)
        self.analytical_policy = self.analytical_solver.run()
        
        print('\tCreating and running the backward solver')

        # Build backward solver and compute optimal backward policy
        self.backward_solver = self.backward_class(self.instance)
        self.backward_policy = self.backward_solver.run()

    def run(self):
      
        print('Comparing analytical and backward optimal policies')

        # Parse stages k and states x and compare optimal policies
        for k in range(0, self.instance.N):
            for x in range(-self.instance.peak(k), self.instance.peak(k) + 1):
                self.log(k, x)
            self.draw(k)

    def draw(self, k):

        # Draw a scatter graph with the discretized states
        xs = [x for x in range(-1 * self.instance.peak(k) - (self.instance.u - self.instance.l), self.instance.peak(k) + (self.instance.u - self.instance.l) + 1 )]
        aJs = [self.analytical_solver.J(k, x) for x in xs]
        bJs = [self.backward_solver.J(k, x) for x in xs]
        plt.plot(xs, aJs, '--o', color = 'blue', linewidth = 2, markersize = 5, zorder = 2)
        plt.plot(xs, bJs, '-o', color = 'red', linewidth = 4, markersize = 10, zorder = 1)
        plt.xlabel('Inventory level x')
        plt.ylabel('Optimal cost-to-go function J_{}(x)'.format(k))        
        plt.savefig('{}{}_{}.png'.format(self.instance.name, '_modified' if self.instance.modified else '', k))
        plt.close()

    def log(self, k, x):

        # Retrieve optimal analytical policy
        a = self.analytical_policy(k, x)

        # Retrieve optimal backward policy
        b = self.backward_policy(k, x)

        print('\t[{}] Analytical policy $\mu^*_{}({}) = {}$, backward policy $\mu^*_{}({}) = {}$'.format('EQUAL' if a == b else 'DIFFERENT', k, x, a, k, x, b))

    def validate(self):

        # Check if it is the correct validation instance
        if self.instance.name == 'small' and not self.instance.modified:

            print('Validating the analytical and the backward policies of instance {} by hand'.format(self.instance.name))

            try:

                # Check analytical solver with values calculated by hand
                assert self.analytical_solver.J(2, 0)  == 0
                assert self.analytical_solver.J(1, -2)  == 72.5
                assert self.analytical_solver.J(1, -1)  == 52.5
                assert self.analytical_solver.J(1, 0)  == 32.5
                assert self.analytical_solver.J(1, 1)  == 12.5
                assert self.analytical_solver.J(1, 2)  == 5
                assert self.analytical_solver.J(1, 3)  == 15
                assert self.analytical_solver.J(0, 0) == 67.5

                # Check backward solver with values calculated by hand
                assert self.backward_solver.J(2, 0)  == 0
                assert self.backward_solver.J(1, -2)  == 72.5
                assert self.backward_solver.J(1, -1)  == 52.5
                assert self.backward_solver.J(1, 0)  == 32.5
                assert self.backward_solver.J(1, 1)  == 12.5
                assert self.backward_solver.J(1, 2)  == 5
                assert self.backward_solver.J(1, 3)  == 15
                assert self.backward_solver.J(0, 0) == 67.5

                print('\tThe analytical and backward solvers MATCH the values computed by hand')

            except:
                print('\tThe analytical and backward solvers DO NOT match the values computed by hand')