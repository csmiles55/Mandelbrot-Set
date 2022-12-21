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

# create the x, y, and z coordinates of the points in the Mandelbrot set
x = np.linspace(-2, 1, 1000)
y = np.linspace(-1.5, 1.5, 1000)
z = np.empty(len(x) * len(y))

for i, x_val in enumerate(x):
    for j, y_val in enumerate(y):
        z[i*len(y) + j] = mandelbrot(x_val, y_val, max_iterations=1000)

# create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z.reshape((len(x), len(y))))
plt.show()
