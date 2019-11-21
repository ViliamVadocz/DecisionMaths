import matplotlib.pyplot as plt

from numpy import gradient
from math import factorial

from autograd import grad, elementwise_grad
import autograd.numpy as np

# Not used
def differentiate(x, y):
    dx_dt = gradient(x)
    dy_dt = gradient(y)

    dy_dx = dy_dt / dx_dt

    return dy_dx

class MyFunction:
    def __init__(self, func=lambda x: 0):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    
    def __add__(self, other):
        def summed(*args, **kwargs):
            return self(*args, **kwargs) + other(*args, **kwargs)
        return MyFunction(summed)

def maclaurin(func, degree : int):
    def term(const, power):
        return lambda x: const * x**power

    expansion = MyFunction()

    for r in range(degree):
        k = func(0.0) / factorial(r)
        expansion = expansion + term(k, r)
        func = grad(func)

    return expansion


# TODO Taylor expansion

# Test
def f(x):
    return np.sin(x) - np.exp(-x/5)

expansion = maclaurin(f, 20)

x = np.linspace(-20.0, 20.0, 1000)
y1 = f(x)
y2 = expansion(x)

# Removing points that are outside the bounds we are interested in.
bound = 10
y1[abs(y1) > bound] = None
y2[abs(y2) > bound] = None 

# Plot
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()