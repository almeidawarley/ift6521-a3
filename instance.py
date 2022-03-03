import statistics as st

class Instance:

    def __init__(self, path, switch = True):

        # Open file with instance information
        with open(path) as content:
            
            # Store N, l, u, c_k, p_k, h_k
            self.N = int(content.readline())
            self.l = int(content.readline())
            self.u = int(content.readline())
            self.c = self.format_row(content)
            self.p = self.format_row(content)
            self.h = self.format_row(content)

        # Compute average c, p, h over stages
        self.avg_c = round(st.mean(self.c), 2)
        self.avg_p = round(st.mean(self.p), 2)
        self.avg_h = round(st.mean(self.h), 2)

        # Start switch to modify instance
        self.switch = switch

        # Store maximum inventory level
        self.peak = self.N * self.u

    def format_row(self, content):

        # Format row from file as a list        
        entries = []
        for entry in content.readline().split():
            entries.append(float(entry))
        return entries

    def flip(self):

        # Flip the switch of the instance
        self.switch = not self.switch

    def __str__(self):

        # Return instance information as string
        payload = '# -----------------------------------------------\n'
        payload += '\tMaximum number of stages (N): {}\n'.format(self.N)
        payload += '\tUniform distribution: U({}, {})\n'.format(self.l, self.u)
        payload += '\tUnit ordering costs (c): {}\n'.format(self.avg_c)
        payload += '\tUnit shortage costs (p): {}\n'.format(self.avg_p)
        payload += '\tUnit storage costs (h): {}\n'.format(self.avg_h)
        payload += '# -----------------------------------------------'

        return payload

    def r(self, k, x):

        # Compute cost of inventory level x at stage k
        return self.avg_p * max(0, -1 * x) + self.avg_h * max(0, x)

    def d(self, k, u):
        
        # Compute cost of ordering u units at stage k
        return self.avg_c * u