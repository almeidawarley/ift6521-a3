import math as mt

class Analytical:

    def __init__(self, problem):

        # Store instance object
        self.instance = problem

        # Create memory for G, H, J, S
        self.computed_G = {}
        self.computed_H = {}
        self.computed_J = {}
        self.computed_S = {}

        # Start memory as empty        
        for k in range(0, self.instance.N):
            self.computed_G[k] = {}
            self.computed_H[k] = {}
            self.computed_J[k] = {}

    def run(self):

        # Run analytical form algorithm
        for k in reversed(range(0, self.instance.N)):
            self.S(k)

        # Create optimal policy function        
        def u(k, x):
            return max( -1 * self.instance.e, self.computed_S[k] - x)
        
        # Return optimal policy function
        return u

    def S(self, k, interval = 3):

        try:
            self.computed_S[k]

        except:

            # Compute the value of S_k
            # (the minimum of G_k(y))

            # Start the bisection method

            # Store the lower border
            a = -self.instance.peak(0)
            # Store the upper border
            b = + self.instance.peak(0)
            # Store the middle value
            c = int(round((b + a) / 2))

            # Loop until reaching interval
            while b - a > interval:

                ac = mt.floor((a + c) / 2)
                cb = mt.ceil((b + c) / 2)

                if self.G(k, ac) <= self.G(k, c):
                    a = a
                    b = c
                    c = ac
                elif self.G(k, c) <= self.G(k, cb):
                    a = ac
                    b = cb
                    c = c
                else:
                    a = c
                    b = b
                    c = cb
            
            # Search linearly in the interval

            min_y = a
            min_G = self.G(k, a)

            for loc_y in range(a + 1, b + 1):
                loc_G = self.G(k, loc_y)
                if min_G > loc_G:
                    min_y = loc_y
                    min_G = loc_G

            self.computed_S[k] = min_y

        return self.computed_S[k]

    def H(self, k, y):

        try:
            self.computed_G[k][y]

        except:

            # Compute the value of H(y) inside G_k(y)

            payload = 0

            for w in range(self.instance.l, self.instance.u + 1):

                probability  = 1 / (self.instance.u - self.instance.l + 1)
                payload += probability * self.r(k, y - w)
                payload += probability * self.J(k + 1, y - w)

            self.computed_H[k][y] = payload

        return self.computed_H[k][y]


    def G(self, k, y):

        try:
            self.computed_G[k][y]

        except:

            # Compute the value of G_k(y)

            payload = self.t(k, y)
            payload += self.H(k, y)            
            payload = round(payload, 2)

            self.computed_G[k][y] = payload

        return self.computed_G[k][y]


    def J(self, k, x):

        if k == self.instance.N:
            return 0

        try:
            self.computed_J[k][x]

        except:

            # Compute the value of J_k(x)

            payload = 0

            if k < self.instance.N:
                payload = self.G(k, x + max(-1 * self.instance.e, self.computed_S[k] - x)) - self.t(k, x)

            self.computed_J[k][x] = payload

        return self.computed_J[k][x]

    def r(self, k, z):

        # Compute the value of r(z)

        return self.instance.p * max(0, -1 * z) + self.instance.h * max(0, z)

    def t(self, k, u):
        
        # Compute the value of t(u)

        return self.instance.c * u