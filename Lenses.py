from math import sin, asin

prob_case   = None

### Lens / Mirrors  ### prob_case = 0
# (1/p) + (1/q) = (1/f)
# M = -(q/p) = h'/h

p           = None
q           = None
f           = None
r           = None
M           = None
obj_h       = None
img_h       = None

#### Refraction     ### prob_case = 1
# n = c / v
# n1 * sin(theta1) = n2 * sin(theta2)
# arcsin(n2/n1),  n1 > n2

c           = 299792458 # m/s
v           = None
n1          = None
n2          = None
theta1      = None
theta2      = None

prob_case = input("What case are you solving?\n"
                    "Case 1: Lenses or Mirrors\n"
                    "Case 2: Refraction\n"
                    "Case: ")

if prob_case == 1:
    print("Enter what you are looking for.")
    looking_for = input()
elif prob_case == 2:
    pass
else:
    print("invalid input")
