import math as mt

class Analytical:

    def __init__(self, problem):

        self.instance = problem

        self.computed_S = {}
        self.computed_G = {}
        self.computed_J = {}
        
        for k in range(0, self.instance.N):
            self.computed_G[k] = {}
            self.computed_J[k] = {}

    def run(self):

        for k in reversed(range(0, self.instance.N)):

            self.S(k)

        payload = ''

        for k in range(0, self.instance.N):
            payload += 'S[{}] = {}; '.format(k, self.computed_S[k])

        print('Analytical form: {}'.format(payload))
        
        def u(k, x):
            return max(self.computed_S[k] - x, -1 * self.instance.e)
        
        return u

    def S(self, k, interval = 3):

        try:
            self.computed_S[k]

        except:

            # Bisection method to find interval

            a = -self.instance.peak
            b = + self.instance.peak
            c = int(round((b + a) / 2))

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
            
            # Linear search over the interval

            min_y = a
            min_G = self.G(k, a)

            for loc_y in range(a + 1, b + 1):
                loc_G = self.G(k, loc_y)
                if min_G > loc_G:
                    min_y = loc_y
                    min_G = loc_G

            # print('> Computed S_{} = {}'.format(k, min_y))

            self.computed_S[k] = min_y

        return self.computed_S[k]


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

            payload = 0

            if k < self.instance.N:
                payload = self.G(k, x + max(-1 * self.instance.e, self.computed_S[k] - x)) - self.instance.t(k, x)
            
            # print('> Computed J_{}({}) = {}'.format(k, x, payload))

            self.computed_J[k][x] = payload

        return self.computed_J[k][x]