import statistics as st

class Instance:

    def __init__(self, path):

        with open(path) as content:
            self.N = int(content.readline())
            self.l = int(content.readline())
            self.u = int(content.readline())
            self.c = self.format_row(content)
            self.p = self.format_row(content)
            self.h = self.format_row(content)

        self.avg_c = round(st.mean(self.c), 2)
        self.avg_p = round(st.mean(self.p), 2)
        self.avg_h = round(st.mean(self.h), 2)

        self.peak = self.N * self.u

    def format_row(self, content):
        
        entries = []
        for entry in content.readline().split():
            entries.append(float(entry))
        return entries

    def __str__(self):

        payload = '# -----------------------------------------------\n'
        payload += '\tMaximum number of stages (N): {}\n'.format(self.N)
        payload += '\tUniform distribution: U({}, {})\n'.format(self.l, self.u)
        payload += '\tUnit ordering costs (c): {}\n'.format(self.avg_c)
        payload += '\tUnit shortage costs (p): {}\n'.format(self.avg_p)
        payload += '\tUnit storage costs (h): {}\n'.format(self.avg_h)
        payload += '# -----------------------------------------------'

        return payload

    def r(self, k, x):

        return self.avg_p * max(0, -1 * x) + self.avg_h * max(0, x)

    # def r(self, k, x):

    #    return self.p[k] * max(0, -1 * x) + self.h[k] * max(0, x)

    def d(self, x):

        return self.avg_c * x