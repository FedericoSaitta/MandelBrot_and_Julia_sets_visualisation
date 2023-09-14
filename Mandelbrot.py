import matplotlib.pyplot as plt
import numpy as np

class Complex:
    def __init__(self, a, b):
        self.re = a
        self.im = b

    def get_re(self):
        return self.re

    def get_im(self):
        return self.im


# f(z) -> z**2 + c and we want to change c
# Goal is to optimize this such that is quick
def convergence_check(c, number = 0, iterations = 0):

# This does not converge so will return a colour other than black
    if number.__abs__() > 2:
        return [iterations*5]
# This does converge so will return black
    if iterations == 50: # for now iterations = 50 and iterations *5 produces a nice result
        return [0]  # too many iterations i dont think is useful and does not produce such good colours

    result = number**2 + c
    iterations += 1

    return convergence_check(c, result, iterations)

# Generate a bunch of numbers

Re = []
Im = []
cols = []

for a in np.arange(-2.2, 0.7, 0.001):
    for b in np.arange(-1.5, 1.5, 0.001):
        obj = Complex(a, b)
        cols.append(convergence_check((obj.re + obj.im * 1j)))
        Re.append(a)
        Im.append(b)

plt.scatter(Re, Im, c = cols , s = 1)
plt.savefig('plot4.png', dpi=1000, bbox_inches='tight')

## For tomorrow to work on:
# Better plotting system (is able to zoom, function that remaps iterations to 0-255 scale
# detail the graph with legend and labels
# create possiblity of julia sets
# zooming in alot?