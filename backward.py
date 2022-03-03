import math as mt

class Backward:

    def __init__(self, i):

        self.instance = i

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

            payload = self.instance.d(k, y)

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

            min_u = 0
            min_J = self.G(k, x + min_u) - self.instance.d(k, x)

            for u in range(1, 2 * self.instance.peak):

                j = self.G(k, x + u) - self.instance.d(k, x)

                if min_J > j:
                    min_u = u
                    min_J = j

            # print('> Computed J_{}({})'.format(k, x))

            self.computed_J[k][x] = min_J
            self.computed_u[k][x] = min_u

        return self.computed_J[k][x]