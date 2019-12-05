import numpy as np
import matplotlib.pyplot as plt

def cubic_spline(points, s, n : int):
    t = np.linspace(0, 1, n)[:, np.newaxis]

    x = points[:, 0]
    x1 = x[:-1]
    x2 = x[1:]
    s_x = s[:, 0]
    s1_x = s_x[:-1]
    s2_x = s_x[1:]

    y = points[:, 1]
    y1 = y[:-1]
    y2 = y[1:]
    s_y = s[:, 1]
    s1_y = s_y[:-1]
    s2_y = s_y[1:]

    a_x = x1
    b_x = s1_x
    c_x = 3*(x2 - x1) - 2*s1_x - s2_x
    d_x = 2*(x1 - x2) + s1_x + s2_x

    a_y = y1
    b_y = s1_y
    c_y = 3*(y2 - y1) - 2*s1_y - s2_y
    d_y = 2*(y1 - y2) + s1_y + s2_y

    x_t = a_x + b_x*t + c_x*t**2 + d_x*t**3
    y_t = a_y + b_y*t + c_y*t**2 + d_y*t**3

    x_final = np.hstack(x_t.T)[:, np.newaxis]
    y_final = np.hstack(y_t.T)[:, np.newaxis]
    curve = np.hstack((x_final, y_final))

    print(curve)
    # Some repeated points at joints
    # FIXME

    return curve

points = np.array([
    [0, 0],
    [3, 1],
    [4, 3],
    [4, 6],
    [6, 2],
    [8, -1],
    [4, -3],
    [2, -1],
    [0, 0]
])

s = np.array([
    [-2, 5],
    [3, 1],
    [3, 1],
    [4, 0],
    [-2, -4],
    [1, -6],
    [-4, 1],
    [-3, 1],
    [-2, 5]
])

curve = cubic_spline(points, s, 100)

plt.scatter(points[:,0], points[:,1])
plt.plot(curve[:,0], curve[:,1])
plt.show()