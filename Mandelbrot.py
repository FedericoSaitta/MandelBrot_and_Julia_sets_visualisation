import matplotlib.pyplot as plt
import numpy as np

convergence_radius = 2
power = 2
max_iter = 80

# Setting which part of the graph to focus on
x_vals = (-2 , 2)
y_vals = (-1, 1)

# Resolution of the image
Width = 4000
Height = 4000

colormap = 'viridis_r'

def mandelbrot(c):
    z = 0
    iterations = 0
    while z.__abs__() < convergence_radius and iterations < max_iter:
        z = z**power + c
        iterations += 1
    return iterations

def julia(z, c = -0.7 - 0.3*1j):
    num = z
    iterations = 0
    while num.__abs__() < convergence_radius  and iterations < max_iter:
        num = num ** power + c
        iterations += 1
    return iterations


x_range , y_range = np.linspace(x_vals[0], x_vals[1], Width), np.linspace(y_vals[0], y_vals[1], Height)
iteration_array  = []

for y in y_range:
    row = []
    for x in x_range:
        c = complex(x + 1j * y)
        row.append(mandelbrot(c)) # Choose whether you want to plot Julia or Mandelbrot sets

    iteration_array.append(row)

ax = plt.axes()
ax.set_aspect('equal')
graph = ax.pcolormesh(x_range, y_range, iteration_array, cmap = colormap)
plt.colorbar(graph)
plt.xlabel("Real-Axis")
plt.ylabel("Imaginary-Axis")
plt.title('Multibrot set for $z_{{new}} = z^{{{}}} + c$'.format(power))
plt.savefig("MandelBrot4k_80iters", dpi = 4000)
