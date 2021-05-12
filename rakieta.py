import numpy as np
from matplotlib import pyplot as plt
import dane as d

# zmienne globalne
g = 9.81


class MNum:
    def calkowanie(self, f):
        fun = [0]
        for i in range(2, len(f[1]) + 1):
            g = np.trapz(f[1][:i], f[0][:i])
            fun += [g]
        return fun


class rakieta(MNum):
    def __init__(self, a, B, c):
        self.m = a
        self.F = B
        self.b = c

    def obliczenia(self):
        self.F[1] = list(map(lambda x, y: np.e ** (self.b / self.m * y) * (x / self.m - g), self.F[1], self.F[0]))
        self.F[1] = self.calkowanie(self.F)
        self.F[1] = list(map(lambda x, y: np.e ** (-self.b/self.m*y) * x, self.F[1], self.F[0]))
        self.F[1] = self.calkowanie(self.F)

    def rysujWykres(self):
        plt.plot(self.F[0], self.F[1])
        plt.show()


with open(d.name) as f:
    T = (f.read()).split()
    T = list(map(lambda x: x.replace(',', '.'), T))
    T = T[4:]

    p = 0
    f = [[], []]
    for i in T:
        f[p] += [float(i)]
        p += 1
        p %= 2
    print(f)

p = 0
while f[1][p] < g/d.m:
    f[1][p] = g/d.m
    p += 1

for i in range(30):
    f[1] += [0]
    f[0] += [f[0][-1] + 0.1]

print(f[0])
print(f[1])

R1 = rakieta(1, f, 2)
R1.obliczenia()
R1.rysujWykres()

