import statistics as st

class Instance:

    def __init__(self, path, switch = True):

        # Open file with instance information
        with open(path) as content:
            
            # Store N, l, u, c, p, h, d
            self.N = int(content.readline())
            self.l = int(content.readline())
            self.u = int(content.readline())
            self.c = int(content.readline())
            self.p = int(content.readline())
            self.h = int(content.readline())
            self.e = int(content.readline())

            # Some sort of cost to dispose items
            # self.d = int(content.readline())

        # Start switch to modify instance
        self.switch = switch

        # Store maximum inventory level
        self.peak = self.N * self.u

    def flip(self):

        # Flip the switch of the instance
        self.switch = not self.switch

    def __str__(self):

        # Return instance information as string
        payload = '# -----------------------------------------------\n'
        payload += '\tMaximum number of stages (N): {}\n'.format(self.N)
        payload += '\tUniform distribution: U({}, {})\n'.format(self.l, self.u)
        payload += '\tUnit ordering costs (c): {}\n'.format(self.c)
        payload += '\tUnit shortage costs (p): {}\n'.format(self.p)
        payload += '\tUnit storage costs (h): {}\n'.format(self.h)
        payload += '# -----------------------------------------------'

        return payload

    def r(self, k, x):

        # Compute cost of inventory level x at stage k
        return self.p * max(0, -1 * x) + self.h * max(0, x)
        # return self.p[k] * max(0, -1 * x) + self.h[k] * max(0, x)

    def t(self, k, u):
        
        # Compute cost of ordering u units at stage k
        return self.c * u
        # return self.c[k] * u