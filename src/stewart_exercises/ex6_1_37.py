#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x * np.sin(x**2)


x = np.linspace(0.0, 4.0)  # 100 values between -0.5 and 3.0

y = f(x)  # evaluate f on the x points

fig = plt.figure()  # manually create a figure
lines = plt.plot(x, y)  # plot data

plt.show()
