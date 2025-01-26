#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x):
    return x * (x**2 - 1) ** 3


def F(x):
    return (x**2 - 1) ** 4 / 8


x = np.linspace(-2, 2, 100)

y = f(x)
w = F(x)

fig, ax = plt.subplots()

l1 = ax.plot(x, y, "b", label="$f(x) = x(x^2 - 1)^3$")
l2 = ax.plot(x, w, "r", label="$F(x) = \\frac{{(x^2 - 1)^4}}{{8}}$")

ax.axis([-2, 2, -2, 2])
ax.set_title("Stewart Ex. 5.5.49")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
ax.grid()

plt.show()
