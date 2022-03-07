import statistics as st

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

            self.modified = version

            if self.modified:
                self.frontier = float(content.readline())
                self.d = float(content.readline())

        # Store reasonable inventory peak
        self.peak = self.N * self.u

        print(self)

    def __str__(self):

        # Return instance information as string
        payload = '# -----------------------------------------------\n'
        payload += '\tNumber of stages (N): {}\n'.format(self.N)
        payload += '\tUniform distribution: U({}, {})\n'.format(self.l, self.u)
        payload += '\tUnit ordering costs (c): {}\n'.format(self.c)
        payload += '\tUnit shortage costs (p): {}\n'.format(self.p)
        payload += '\tUnit storage costs (h): {}\n'.format(self.h)
        payload += '\tReturnable units (e): {}\n'.format(self.e)
        payload += '\tInventory peak (peak): {}\n'.format(self.peak)        
        if self.modified:
            payload += '\tWorking with modified version\n'
            payload += '\tFrontier for changing: {}\n'.format(self.frontier)
            payload += '\tUnit ordering costs (d): {}\n'.format(self.d)
        else:
            payload += '\tWorking with standard version\n'
        payload += '# -----------------------------------------------'

        return payload