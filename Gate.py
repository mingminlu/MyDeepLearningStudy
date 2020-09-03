import numpy as np


def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.7, 0.5])
    b = -0.5
    y = np.sum(w*x) + b
    if y <= 0:
        return 0
    else:
        return 1


def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.7, -0.5])
    b = 0.5
    y = np.sum(w * x) + b
    if y <= 0:
        return 0
    else:
        return 1


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.6,0.6])
    b = -0.5
    y = np.sum(w * x) + b
    if y <= 0:
        return 0
    else:
        return 1


def gate(x1, x2, w1, w2, b):
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    y = np.sum(w * x) + b
    if y <= 0:
        return 0
    else:
        return 1


print(and_gate(0, 1))
print(nand_gate(0, 0))
print(or_gate(0, 0))


print(gate(0, 1, 0.7, 0.7, -0.8))
print(gate(1, 1, -0.7, -0.7, 0.8))
print(gate(0, 1, 0.5, 0.4, -0.3))