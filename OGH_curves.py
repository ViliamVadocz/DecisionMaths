'''Optimised Geometric Hermite Curves'''
#http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.1622&rep=rep1&type=pdf

import numpy as np
import matplotlib.pyplot as plt

p1 = np.array([[-2],[-2]])
t1 = np.array([[-3],[1]])
p2 = np.array([[2],[2]])
t2 = np.array([[2],[3]])

def hermite(p1,p2,t1,t2,t):
    h1 = 2*t**3 - 3*t**2 + 1
    h2 = -2*t**3 + 3*t**2
    h3 = t**3 - 2*t**2 + t
    h4 = t**3 -  t**2
    p = h1 * p1 + h2 * p2 + h3 * t1 + h4 * t2
    return p

n = 100
a = np.linspace(0.0,1.0,n)
b = hermite(p1,p2,t1,t2,a)

plt.plot(b[0],b[1])
plt.plot([p1[0],t1[0]],[p1[1],t1[1]])
plt.plot([p2[0],t2[0]],[p2[1],t2[1]])
plt.show()

