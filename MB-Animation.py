import numpy as np
from PIL import Image
from numba import jit
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

RES = 500


@jit
def make_mandelbrot(x_range, y_range):
    max_iterations = 50
    result = np.zeros((RES, RES))
    # for each pixel at (ix, iy)
    j = 0
    for iy in y_range:
        i = 0

        for ix in x_range:
            x0 = ix
            y0 = iy

            x = 0.0
            y = 0.0
            # perform Mandelbrot set iterations
            for iteration in range(max_iterations):
                x_new = x*x - y*y + x0
                y = 2*x*y + y0
                x = x_new

                # if escaped
                if x*x + y*y > 4.0:
                    # color using pretty linear gradient
                    color = 1.0 - 0.01 * \
                        (iteration - np.log2(np.log2(x*x + y*y)))
                    break
            else:
                # failed, set color to black
                color = 0.0

            result[j, i] = color
            i += 1
        j += 1

    return result


fig = plt.figure()

x_vals = (-2.2, 1)
y_vals = (-1.1, 1.1)


frame_num = 200

zoom_coords = (1.75, 0)

up_increment_x = np.abs((x_vals[0] - zoom_coords[0]) / frame_num)
up_increment_y = np.abs((y_vals[0] - zoom_coords[1]) / frame_num)

down_increment_x = np.abs((x_vals[1] - zoom_coords[0]) / frame_num)
down_increment_y = np.abs((y_vals[1] - zoom_coords[1]) / frame_num)

colour = []

for frame in range(frame_num):
    r = x_vals[0] + up_increment_x * frame
    l = x_vals[1] - down_increment_x * frame
    t = y_vals[0] + up_increment_y * frame
    b = y_vals[1] - down_increment_y * frame

    x_range = np.linspace(l, r, RES)
    y_range = np.linspace(b, t, RES)

    colour.append(make_mandelbrot(x_range, y_range))


colour = np.array(colour)
cax = plt.pcolormesh(
    x_range, y_range, colour[0, :, :], cmap='hsv_r')


def animate(i):
    cax.set_array(colour[i, :, :].flatten())


anim = FuncAnimation(fig, animate, frames=frame_num, interval=20)
anim.save('MandelBrot_Zoom.mp4',
          writer='ffmpeg', fps=20)
print('Animation has been saved')
