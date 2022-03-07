import math as mt

class Backward:

    def __init__(self, problem):

        # Store instance object
        self.instance = problem

        # Create memory for H, J, u
        self.computed_H = {}
        self.computed_J = {}
        self.computed_u = {}

        # Start memory as empty        
        for k in range(0, self.instance.N):
            self.computed_H[k] = {}
            self.computed_J[k] = {}
            self.computed_u[k] = {}

    def run(self):

        # Run backward chaining algorithm
        for k in reversed(range(0, self.instance.N)):
            for x in range(-1 * self.instance.peak, self.instance.peak + 1):                
                self.J(k, x)

        # Create optimal policy function
        def u(k, x):
            try:
                self.computed_u[k][x]
            except:
                print('Optimal policy for inventory level {} at stage {} not calculated in the discretization'.format(x, k))
                exit()
            return self.computed_u[k][x]
        
        # Return optimal policy function
        return u

    def H(self, k, y):

        try:
            self.computed_G[k][y]

        except:

            # Compute the value of H(y) inside G_k(y)

            payload = 0

            for w in range(self.instance.l, self.instance.u + 1):

                probability  = (w - self.instance.l + 1)/(self.instance.u - self.instance.l + 1)
                payload += probability * self.r(k, y - w)
                payload += probability * self.J(k + 1, y - w)

            self.computed_H[k][y] = payload

        return self.computed_H[k][y]


    def J(self, k, x):

        if k == self.instance.N:
            return 0

        try:
            self.computed_J[k][x]

        except:

            # Compute the value of J_k(x)

            min_u = - self.instance.e
            min_J = self.t(k, min_u) + self.H(k, x + min_u)

            for u in range(- 1 * self.instance.e + 1, 2 * self.instance.peak):

                j = self.t(k, u) + self.H(k, x + u)

                if min_J > j:
                    min_u = u
                    min_J = j

            self.computed_J[k][x] = min_J
            self.computed_u[k][x] = min_u

        return self.computed_J[k][x]

    def r(self, k, z):

        # Compute the value of r(z)

        return self.instance.p * max(0, -1 * z) + self.instance.h * max(0, z)

    def t(self, k, u):
        
        # Compute the value of t(u)

        if self.instance.modified:

            if u <= self.instance.frontier:

                return self.instance.c * u

            else:

                return self.instance.d * u

        else:

            return self.instance.c * u