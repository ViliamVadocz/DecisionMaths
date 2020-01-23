import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = 100
n = 1000

t = np.linspace(-1.0, 1.0, n)
x = np.sqrt(1 - t**2) * np.cos(t * f)
y = np.sqrt(1 - t**2) * np.sin(t * f)
z = t

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()