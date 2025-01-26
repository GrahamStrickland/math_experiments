#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x):
    return x**3 * np.sqrt(1 + x**2)


def F(x):
    return (1 + x**2) ** (5 / 2) / 5 - (1 + x**2) ** (3 / 2) / 3


x = np.linspace(-2, 2)

y = f(x)
i = F(x)

fig, ax = plt.subplots()

l1 = ax.plot(x, y, "b")
l2 = ax.plot(x, i, "r")

ax.axis([-2, 2, -2, 2])
ax.set_title("Stewart Ex. 7.1.45")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend((r"$y = x^3 \sqrt{1 + x^2}$", r"$y = \int x^3 \sqrt{1 + x^2} \mathrm{d}x"))
ax.grid()

plt.show()
