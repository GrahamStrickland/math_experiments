import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-8, 8, 0.1)


def f(t):
    return t**4 + 3 * t**3 - 12 * t**2 + t - 6


fig, ax = plt.subplots()
ax.plot(t, f(t))
ax.set_title(
    "Theoretical Minimum: Interlude 1 - Exercise 1\nGraph of $f(t) = t^4 + 3t^3 - 12t^2 + t - 6$",
    usetex=True,
)
ax.set_xlabel("$t$", usetex=True)
ax.set_ylabel("$f(t)$", usetex=True)

fig.savefig("i01ex01a.png", dpi=300)
