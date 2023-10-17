import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


convergence_radius = 2
power = 2
max_iter = 80

# Setting which part of the graph to focus on
x_vals = (-2.5, 1)
y_vals = (-1.5, 1.5)

# Number of data points, total it n x n
data_points = 10

colormap = 'viridis_r'


def mandelbrot(c):
    z = 0
    iterations = 0
    while z.__abs__() < convergence_radius and iterations < max_iter:
        z = z**power + c
        iterations += 1
    return iterations


fig = plt.figure()
ax = plt.axes()

x_range = np.linspace(x_vals[0], x_vals[1], data_points)
y_range = np.linspace(y_vals[0], y_vals[1], data_points)


iteration_array = []
for depth in range(10):  # Note the size of the depth should match the frames
    width = []
    for y in y_range:
        row = []
        for x in x_range:
            c = complex(x + 1j * y)
            # Choose whether you want to plot Julia or Mandelbrot sets
            row.append(mandelbrot(c))
        width.append(row)
    iteration_array.append(width)


iteration_array = np.array(iteration_array)

cax = ax.pcolormesh(
    x_range, y_range, iteration_array[:-1, :-1, 0], cmap=colormap)
fig.colorbar(cax)


def animate(i):
    cax.set_array(iteration_array[:-1, :-1, i].flatten())


anim = FuncAnimation(fig, animate, frames=10, interval=20)
anim.save('continuousSineWave.mp4',
          writer='ffmpeg', fps=30)
