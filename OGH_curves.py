'''Optimised Geometric Hermite Curves'''
# http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.104.1622&rep=rep1&type=pdf

import numpy as np
import matplotlib.pyplot as plt

def angle_between_vectors(a, b):
    """Returns the angle in radians between vectors a and b"""
    angle_a = np.arctan2(a[1], a[0])
    angle_b = np.arctan2(b[1], b[0])
    return abs(angle_b - angle_a)[0]

def vector_from_angle(angle : float, magnitude : float = 1):
    """Returns a vector with a given angle and length"""
    return magnitude * np.array([np.cos(angle),np.sin(angle)])

def Q(p0, p1, v0, v1, t0, t1, t):
    """Basic Hermite curve."""
    s = (t-t0)/(t1-t0)
    h0 = (2*s+1)*(s-1)*(s-1)
    h1 = (-2*s+3)*s*s
    h2 = (1-s)*(1-s)*s*(t1-t0)
    h3 = (s-1)*s*s*(t1-t0)
    return h0*p0 + h1*p1 + h2*v0 + h3*v1

def OGH(p0, p1, v0, v1, t0, t1, t):
    """Optimized geometric Hermite curve."""
    s = (t-t0)/(t1-t0)
    a0 = (6*np.dot((p1-p0).T,v0)*np.dot(v1.T,v1) - 3*np.dot((p1-p0).T,v1)*np.dot(v0.T,v1)) / ((4*np.dot(v0.T,v0)*np.dot(v1.T,v1) - np.dot(v0.T,v1)*np.dot(v0.T,v1))*(t1-t0))
    a1 = (3*np.dot((p1-p0).T,v0)*np.dot(v0.T,v1) - 6*np.dot((p1-p0).T,v1)*np.dot(v0.T,v0)) / ((np.dot(v0.T,v1)*np.dot(v0.T,v1) - 4*np.dot(v0.T,v0)*np.dot(v1.T,v1))*(t1-t0))
    h0 = (2*s+1)*(s-1)*(s-1)
    h1 = (-2*s+3)*s*s
    h2 = (1-s)*(1-s)*s
    h3 = (s-1)*s*s
    return h0*p0 + h1*p1 + h2*v0*a0 + h3*v1*a1

def COH(p0, p1, v0, v1, t0, t1, t):
    """Composite optimized geometric Hermite curve."""
    # theta is the counterclockwise angle from the vector p0p1 to v0.
    # phi is the counterclockwise angle from the vector p0p1 to v1.
    theta = angle_between_vectors(p1-p0, v0)
    phi = angle_between_vectors(p1-p0, v1)

    print("theta: {}pi".format(theta/np.pi))
    print("phi: {}pi".format(phi/np.pi))

    # If tangent direction preserving conditions are met, use an OGH.
    if 3*np.cos(theta) > np.cos(theta - 2*phi) and 3*np.cos(phi) > np.cos(phi - 2*theta):
        return OGH(p0, p1, v0, v1, t0, t1, t)

    # Method M1 for generating two-segment COH.
    elif (0 <= theta <= np.pi/6) and (np.pi/3 <= phi <= 2*np.pi/3):
        pT = p1 - vector_from_angle(phi/2 + np.arctan2((p1-p0)[1],(p1-p0)[0]), np.linalg.norm(p1-p0)/3)
        ang = angle_between_vectors(pT-p0, p1-pT)
        vT = vector_from_angle(ang/2 + np.arctan2((p1-p0)[1],(p1-p0)[0]))
        return np.concatenate([OGH(p0,pT,v0,vT,t0,t1,t),OGH(pT,p1,vT,v1,t0,t1,t)],axis=1)

    # Method M2 for generating two-segment COH.
    elif ((0 <= theta <= np.pi/3) and (np.pi <= phi <= 5*np.pi/3)) or ((np.pi/3 <= theta <= 2*np.pi/3) and (4*np.pi/3 <= phi <= 5*np.pi/3)):
        # pT = ?
        # vT = ?
        # np.concatenate((OGH(p0,m,v0,vm,t0,t1,t),OGH(m,vm,p1,v1,t0,t1,t)))
        pass


# Parameters.
p0 = np.array([[-1], [-2]])
v0 = np.array([[1], [3]])

p1 = np.array([[1], [0]])
v1 = np.array([[-2], [1]])

t0 = 0
t1 = 1

v0 = v0 / np.linalg.norm(v0)
v1 = v1 / np.linalg.norm(v1)

n : int = 1000
a = np.linspace(t0, t1, n)
b = COH(p0, p1, v0, v1, t0, t1, a)

# Plots curve.
plt.plot(b[0], b[1])

# Plots tangents.
plt.plot([p0[0], (p0+v0)[0]], [p0[1], (p0+v0)[1]], '-r')
plt.plot([p1[0], (p1+v1)[0]], [p1[1], (p1+v1)[1]], '-r')

# Plots p0p1.
plt.plot([p0[0],p1[0]], [p0[1],p1[1]], '-b')

plt.show()
