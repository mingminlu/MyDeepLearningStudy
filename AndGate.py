import numpy as np


def AND(x1, x2, w1, w2, b):
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    y = np.sum(w*x) + b
    if y <= 0:
        return 0
    else:
        return 1


print(AND(1,1,0.5,0.5,-0.7))