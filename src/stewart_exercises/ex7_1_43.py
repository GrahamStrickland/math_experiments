#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x):
    return x * np.exp(-2 * x)


def F(x):
    return (-x / 2) * np.exp(-2 * x) - (1 / 4) * np.exp(-2 * x)


x = np.linspace(-2, 4)

y = f(x)
i = F(x)

fig, ax = plt.subplots()

l1 = ax.plot(x, y, "b")
l2 = ax.plot(x, i, "r")

ax.axis([-2, 4, -2, 2])
ax.set_title("Stewart Ex. 7.1.43")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend((r"$y = xe^{-2x}$", r"$y = \int xe^{-2x} \mathrm{d}x"))
ax.grid()

plt.show()
