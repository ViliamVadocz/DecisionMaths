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

def go_forward(n : int) -> str:
    if n == 0: return 'F'
    return 'F' + go_forward(n-1)

def square_spiral(n : int) -> str:
    if n == 0: return 'R'
    return square_spiral(n-1) + go_forward(n-1) + 'R' + go_forward(n-1)

def some_fractal(n : int) -> str:
    if n == 0: return 'F'
    return p(n-1) + 'LF' + p(n-1) + 'FR' + p(n-1)

def zig() -> str:
    return 'FRFR'

def zag() -> str:
    return 'FLFL'

# Not quite dragon
def dragon(n : int) -> str:
    if n == 0: return zig() + zag()
    return dragon(n-1) + 'L' + dragon(n-1).replace('R','*').replace('L','R').replace('*','L')[::-1]

if __name__ == "__main__":
    robot = Robot()
    trace = robot.execute(dragon(2))
    plt.plot(trace[:,0], trace[:,1])
    plt.show()