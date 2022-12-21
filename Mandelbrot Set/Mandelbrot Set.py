import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(x, y, max_iterations):
    c = x + y*1j
    z = 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iterations

# create the x and y coordinates of the points in the Mandelbrot set
x = np.linspace(-2, 1, 1000)
y = np.linspace(-1.5, 1.5, 1000)

counter = 0

for x_val in x:
    for y_val in y:
        if mandelbrot(x_val, y_val, max_iterations=100) == 100:
            print(x + y*1j)
            counter += 1
        if counter == 10:  # stop after printing 10 numbers
            break
    if counter == 10:  # stop after printing 10 numbers
        break
