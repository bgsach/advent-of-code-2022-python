import numpy as np

def read(day : int):
    with open(f'data/{day:02}.txt') as f:
        return f.read().split()

def readnp(day : int, **kw):
    kw = {'delimiter': ','} | kw
    return np.genfromtxt(f'data/{day:02}.txt', **kw)
