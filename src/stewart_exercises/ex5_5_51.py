#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x):
    return np.exp(np.cos(x)) * np.sin(x)


def F(x):
    return -np.exp(np.cos(x))


x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

y = f(x)
w = F(x)

fig, ax = plt.subplots()

l1 = ax.plot(x, y, "b", label="$f(x) = e^{{\\cos x}}\\sin x$")
l2 = ax.plot(x, w, "r", label="$F(x) = -e^{{\\cos x}}$")

ax.axis([-2 * np.pi, 2 * np.pi, -3, 2])
ax.set_title("Stewart Ex. 5.5.51")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
ax.grid()

plt.show()
