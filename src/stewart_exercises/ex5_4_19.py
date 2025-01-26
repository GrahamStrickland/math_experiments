#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x):
    return np.sin(x) + x**2


x = np.linspace(-np.pi, np.pi)

fig, ax = plt.subplots()
l1 = ax.plot(x, f(x))
l2 = ax.plot(x, f(x) + 1)
l3 = ax.plot(x, f(x) + 2)
l4 = ax.plot(x, f(x) + 3)
l5 = ax.plot(x, f(x) - 1)
l6 = ax.plot(x, f(x) - 2)
l7 = ax.plot(x, f(x) - 3)

ax.set_title("Stewart Ex. 5.4.19")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(
    (
        "$y = \sin x + x^2$",
        "$y = \sin x + x^2 + 1$",
        "$y = \sin x + x^2 + 2$",
        "$y = \sin x + x^2 + 3$",
        "$y = \sin x + x^2 - 1$",
        "$y = \sin x + x^2 - 2$",
        "$y = \sin x + x^2 - 3$",
    )
)
ax.grid()

plt.show()
