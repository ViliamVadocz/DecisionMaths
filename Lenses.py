from math import sin, asin

prob_case   = None

### Lens / Mirrors  ### prob_case = 1
# (1/p) + (1/q) = (1/f)
# M = -(q/p) = h'/h

p           = None
q           = None
f           = None
r           = None
M           = None
obj_h       = None
img_h       = None
vars1       = [p, q, f, r, M, obj_h, img_h]

#### Refraction     ### prob_case = 2
# n = c / v
# n1 * sin(theta1) = n2 * sin(theta2)
# arcsin(n2/n1),  n1 > n2

c           = 299792458 # m/s
v           = None
n1          = None
n2          = None
theta1      = None
theta2      = None
crit_ang    = None
#TODO Use a dictionary?
vars2       = ["velocity", "n1", "n2", "theta1", "theta2", "crit_ang"]

def problem_solver():
    prob_case = input("What case are you solving?\n"
                        "Case 1: Lenses or Mirrors\n"
                        "Case 2: Refraction\n"
                        "Case: ")

    if prob_case == "1":
        looking_for = []

        for var in variables1:
            ans = input(("What is""equal to? (in base SI units)\n"
                        "'U' for unknown"))
            if ans == "U":
                looking_for += [var]
            else:
                var = float(ans)

        print(looking_for)



    elif prob_case == "2":
        looking_for = []

        for var in variables2:
            ans = input("What is",var,"equal to? (in base SI units)\n"
                        "'U' for unknown")
            if ans == "U":
                looking_for += [var]
            else:
                var = float(ans)

        print(looking_for)

    elif prob_case == "exit":
        print("Adios!")

    else:
        print("invalid input")
        problem_solver()


problem_solver()