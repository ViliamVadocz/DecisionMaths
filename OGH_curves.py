'''Optimised Geometric Hermite Curves'''
#http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.1622&rep=rep1&type=pdf

import numpy as np
import matplotlib.pyplot as plt

import numpy as np

def unit_vector(V):
    """ Returns the unit vector of the vector."""
    return V / np.linalg.norm(V)

def angle(a,b):
    """ Returns the angle in radians between vectors a and b"""
    a_u = unit_vector(a)
    b_u = unit_vector(b)
    return np.arccos(np.clip(np.dot(a_u, b_u), -1.0, 1.0))



p0 = np.array([[-1],[1]])
v0 = np.array([[3],[-2]])
p1 = np.array([[1],[1]])
v1 = np.array([[3],[2]])
t0 = 0
t1 = 2

def Q(p0,p1,v0,v1,t0,t1,t):
    s = (t-t0)/(t1-t0)
    h0 = (2*s+1)*(s-1)*(s-1)
    h1 = (-2*s+3)*s*s
    h2 = (1-s)*(1-s)*s*(t1-t0)
    h3 = (s-1)*s*s*(t1-t0)
    return h0*p0 + h1*p1 + h2*v0 + h3*v1

def OGH(p0,p1,v0,v1,t0,t1,t):
    s = (t-t0)/(t1-t0)
    a0 = (6*np.dot((p1-p0).T,v0)*np.dot(v1.T,v1) - 3*np.dot((p1-p0).T,v1)*np.dot(v0.T,v1)) / ((4*np.dot(v0.T,v0)*np.dot(v1.T,v1) - np.dot(v0.T,v1)*np.dot(v0.T,v1))*(t1-t0))
    a1 = (3*np.dot((p1-p0).T,v0)*np.dot(v0.T,v1) - 6*np.dot((p1-p0).T,v1)*np.dot(v0.T,v0)) / ((np.dot(v0.T,v1)*np.dot(v0.T,v1) - 4*np.dot(v0.T,v0)*np.dot(v1.T,v1))*(t1-t0))
    h0 = (2*s+1)*(s-1)*(s-1)
    h1 = (-2*s+3)*s*s
    h2 = (1-s)*(1-s)*s
    h3 = (s-1)*s*s
    return h0*p0 + h1*p1 + h2*v0*a0 + h3*v1*a1

def COH(p0,p1,v0,v1,t0,t1,t):
    # θ is the counterclockwise angle from the vector p0p1 to v0.
    # ϕ is the counterclockwise angle from the vector p0p1 to v1.
    # θ and ϕ are both 2π-periodic (hence, a clockwise angle would be measured in negative degrees).
    theta = angle(p1-p0,v0)
    phi = angle(p1-p0,v1)

    # Tangent direction preserving conditions.
    if 3*np.cos(theta) > np.cos(theta - 2*phi) and 3*np.cos(phi) > np.cos(phi - 2*theta):
        return OGH(p0,p1,v0,v1,t0,t1,t)

    # Method M1 for generating two-segment COH.
    elif  (0 <= theta <= np.pi/6) and (np.pi/3 <= phi <= 2*np.pi/3):
        #m = ?
        #vm = ?
        #np.concatenate((OGH(p0,m,v0,vm,t0,t1,t),OGH(m,vm,p1,v1,t0,t1,t)))
        pass

    # Method M2 for generating two-segment COH.
    elif ((0 <= theta <= np.pi/3) and (np.pi <= phi <= 5*np.pi/3)) or ((np.pi/3 <= theta <= 2*np.pi/3) and (4*np.pi/3 <= phi <= 5*np.pi/3)):
        #m = ?
        #vm = ?
        #np.concatenate((OGH(p0,m,v0,vm,t0,t1,t),OGH(m,vm,p1,v1,t0,t1,t)))
        pass

n = 100
a = np.linspace(t0,t1,n)
b = Q(p0,p1,v0,v1,t0,t1,a)
c = OGH(p0,p1,v0,v1,t0,t1,a)

plt.plot(b[0],b[1])
plt.plot(c[0],c[1])
plt.plot([p0[0],(p0+v0)[0]],[p0[1],(p0+v0)[1]])
plt.plot([p1[0],(p1+v1)[0]],[p1[1],(p1+v1)[1]])
plt.show()

