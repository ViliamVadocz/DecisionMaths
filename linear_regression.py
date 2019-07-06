import numpy as np
import matplotlib.pyplot as plt


def linear_regression(x, y):
    Sxx = np.sum(x * x) - np.sum(x)*np.sum(x) / len(x)
    Sxy = np.sum(x * y) - np.sum(x)*np.sum(y) / len(x)

    b = Sxy / Sxx
    a = np.mean(y) - b*np.mean(x)

    return a, b

def make_line(x, a, b):
    y = a + b*x
    return y


# Generating correlated data
mean    : float = 0.0
std     : float = 1.0
points  : int   = 100

x = np.random.normal(mean, std, points)
y = x + np.random.normal(mean, std, points)

a, b = linear_regression(x, y)

reg_x = np.linspace(mean-3*std, mean+3*std, 100)
reg_y = make_line(reg_x, a, b)

equation = 'y = {} + x * {}'.format("%.2f" % a, "%.2f" % b)

plt.plot(reg_x, reg_y, '-b', label=equation)
plt.scatter(x, y, c='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.show()
