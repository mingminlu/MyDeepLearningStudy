import numpy as np


def andGate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.7, 0.5])
    b = -0.5
    y = np.sum(w*x) + b
    print(y)
    if y <= 0:
        return 0
    else:
        return 1


print(andGate(1,1))