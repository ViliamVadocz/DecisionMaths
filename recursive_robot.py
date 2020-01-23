import numpy as np
import matplotlib.pyplot as plt

# Inspired by https://csat.io/practice/p4/q9

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.trace = [[0,0]]
    
    def execute(self, cmds : str):
        for cmd in cmds:
            if cmd == 'L': self.dir += 1
            if cmd == 'R': self.dir += 3
            if cmd == 'F':
                if self.dir == 0: self.x += 1
                if self.dir == 1: self.y += 1
                if self.dir == 2: self.x -= 1
                if self.dir == 3: self.y -= 1
            self.dir %= 4
            self.trace.append([self.x, self.y])
        return np.array(self.trace)

"""def q(n : int):
    if n == 0: return 'F'
    return 'F' + q(n-1)

def p(n : int):
    if n == 0: return 'R'
    return p(n-1) + q(n-1) + 'R' + q(n-1)"""

def p(n : int):
    if n == 0: return 'F'
    return p(n-1) + 'LF' + p(n-1) + 'FR' + p(n-1)
    

if __name__ == "__main__":
    robot = Robot()
    trace = robot.execute(p(10))
    plt.plot(trace[:,0], trace[:,1])
    plt.show()