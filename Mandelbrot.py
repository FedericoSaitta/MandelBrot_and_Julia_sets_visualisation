import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw



# f(z) -> z**2 + c and we want to change c

def convergence_check(c):

    z = 0
    iterations = 0

    while z.__abs__() < 2 and iterations < 80:
        z = z*z + c
        iterations += 1

    return iterations



Width = 300
Height = 300

# Decides which part of the mandelbrot set to focus on
x_range = (-2.2,0.7) # To view the entire fractal use (-2.2,0.7)
y_range = (-1.5, 1.5)   # To vire the entire fractal use (-1.5, 1.5)


im = Image.new('HSV', (Width, Height), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(Width):
    for y in range(Height):
        c = complex( x_range[0] + (x/Width)*( x_range[1] - x_range[0]),
                     y_range[0] + (y / Height) * (y_range[1] - y_range[0]) )
        m = convergence_check(c)
        # The color depends on the number of iterations
        hue = int(255 * m / 80)
        saturation = 255
        value = 255 if m < 80 else 0
        # Plot the point
        draw.point([x, y], (hue, saturation, value))

draw.text((0, 20) , 'Hello', fill = (0,0,0) )

im.convert('RGB').save('plot4.png', 'PNG')

