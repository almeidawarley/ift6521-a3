import math as mt

class Backward:

    def __init__(self, problem):

        self.instance = problem

        self.computed_G = {}
        self.computed_J = {}
        self.computed_u = {}
        
        for k in range(0, self.instance.N):
            self.computed_G[k] = {}
            self.computed_J[k] = {}
            self.computed_u[k] = {}

    def run(self):

        for k in reversed(range(0, self.instance.N)):
            for x in range(-1 * self.instance.peak, self.instance.peak + 1):
                
                self.J(k, x)

        def u(k, x):
            return self.computed_u[k][x]
        
        return u


    def G(self, k, y):

        try:
            self.computed_G[k][y]

        except:

            payload = self.instance.t(k, y)

            for w in range(self.instance.l, self.instance.u + 1):
                probability  = (w - self.instance.l + 1)/(self.instance.u - self.instance.l + 1)
                payload += probability * self.instance.r(k, y - w)
                payload += probability * self.J(k + 1, y - w)
            
            payload = round(payload, 2)

            # print('> Computed G_{}({}) = {}'.format(k, y, payload))

            self.computed_G[k][y] = payload

        return self.computed_G[k][y]


    def J(self, k, x):

        if k == self.instance.N:
            return 0

        try:
            self.computed_J[k][x]

        except:

            min_y = x - self.instance.e
            min_J = self.G(k, min_y) # - self.instance.t(k, x)

            for y in range(x - self.instance.e + 1, self.instance.peak):

                J = self.G(k, y) # - self.instance.t(k, x)

                if min_J > J:
                    min_y = y
                    min_J = J
                    
            # print('> Computed J_{}({})'.format(k, x))

            self.computed_J[k][x] = min_J - self.instance.t(k, x)
            self.computed_u[k][x] = min_y - x

        return self.computed_J[k][x]