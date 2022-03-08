import os

class Instance:

    def __init__(self, path, version = False):

        print('Reading instance information from file: {}'.format(path))

        # Open file with instance information
        with open(path) as content:
            
            # Store N, l, u, c, p, h, e
            self.N = int(content.readline())
            self.l = int(content.readline())
            self.u = int(content.readline())
            self.c = float(content.readline())
            self.p = float(content.readline())
            self.h = float(content.readline())
            self.e = int(content.readline())

            # Store frontier and d for modified version
            self.modified = version
            if self.modified:
                self.frontier = float(content.readline())
                self.d = float(content.readline())

            # Store name of the instance
            self.name = os.path.basename(path).replace('.txt', '')

        print(self)

    def peak(self, k):

        # Compute most optimistic demand
        return (self.N - k) * self.u

    def __str__(self):

        # Return instance information as string
        payload = '# -----------------------------------------------\n'
        payload += '\tTuple: ({},{},{},{},{},{},{})\n'.format(self.N, self.l, self.u, self.c, self.p, self.h, self.e)
        payload += '\tNumber of stages (N): {}\n'.format(self.N)
        payload += '\tUniform distribution: U({}, {})\n'.format(self.l, self.u)
        payload += '\tUnit ordering costs (c): {}\n'.format(self.c)
        payload += '\tUnit shortage costs (p): {}\n'.format(self.p)
        payload += '\tUnit storage costs (h): {}\n'.format(self.h)
        payload += '\tReturnable units (e): {}\n'.format(self.e)     
        if self.modified:
            payload += '\tWorking with modified version\n'
            payload += '\tFrontier for changing: {}\n'.format(self.frontier)
            payload += '\tUnit ordering costs (d): {}\n'.format(self.d)
        else:
            payload += '\tWorking with standard version\n'
        payload += '# -----------------------------------------------'

        return payload