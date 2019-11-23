import matplotlib.pyplot as plt
from math import factorial
from autograd import grad
import autograd.numpy as np

# My own function class that allows for combining functions into one by summing.
class MyFunction:
    def __init__(self, func=lambda x: 0):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    
    def __add__(self, other):
        def summed(*args, **kwargs):
            return self(*args, **kwargs) + other(*args, **kwargs)
        return MyFunction(summed)

def maclaurin_func(func, degree : int):
    """Find the Maclaurin expansion of the given function to the given degree.
    Returns the function.
    
    Arguments:
        func {function} -- The function which to approximate.
        degree {int} -- Degree of the resulting expansion.
    
    Returns:
        function -- The Maclaurin expansion function.
    """
    def term(const, power):
        return lambda x: const * x**power

    expansion = MyFunction()

    for r in range(degree):
        k = func(0.0) / factorial(r)
        expansion += term(k, r)
        func = grad(func)

    return expansion

def maclaurin_str(func, degree : int):
    """Find the Maclaurin expansion of the given function to the given degree.
    Returns the string representation.
    
    Arguments:
        func {function} -- The function which to approximate.
        degree {int} -- Degree of the resulting expansion.
    
    Returns:
        str -- The Maclaurin expansion string.
    """
    def term(const, power):
        return f'{const:.3f}*(x^{power} /{power}!) + \n'

    expansion = ''

    for r in range(degree):
        expansion += term(func(0.0), r)
        func = grad(func)

    return expansion[:-4]

def taylor_func(func, degree : int, a : float=0.0):
    """Find the Taylor expansion of the given function to the given degree centered at point given by a.
    Returns the function.
    
    Arguments:
        func {function} -- The function which to approximate.
        degree {int} -- Degree of the resulting expansion.
        a {float} -- The point at which to take derivative information.
    
    Returns:
        function -- The Taylor expansion function.
    """
    def term(const, power):
        return lambda x: const * (x - a)**power

    if type(a) is not float:
        a = float(a)

    expansion = MyFunction()

    for r in range(degree):
        k = func(a) / factorial(r)
        expansion += term(k, r)
        func = grad(func)

    return expansion

def taylor_str(func, degree : int, a : float=0.0):
    """Find the Taylor expansion of the given function to the given degree centered at point given by a.
    Returns the string representation.
    
    Arguments:
        func {function} -- The function which to approximate.
        degree {int} -- Degree of the resulting expansion.
        a {float} -- The point at which to take derivative information.
    
    Returns:
        str -- The Taylor expansion string.
    """
    def term(const, power):
        if a >= 0:
            return f'{const:.3f}*((x-{a})^{power} /{power}!) + \n'
        else:
            return f'{const:.3f}*((x+{-a})^{power} /{power}!) + \n'


    if type(a) is not float:
        a = float(a)

    expansion = ''

    for r in range(degree):
        expansion += term(func(a), r)
        func = grad(func)

    return expansion[:-4]

# Test
def f(x):
    return np.exp(x/10) * np.sin(4*x)

deg = 10
# expansion = maclaurin_func(f, deg)
# string = maclaurin_str(f, deg)
# print(string)

a = -3
expansion = taylor_func(f, deg, a)
string = taylor_str(f, deg, a)
print(string)

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