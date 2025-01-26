import matplotlib.pyplot as plt
import numpy as np
from numpy import pi as pi

x = np.arange(-2 * pi, 2 * pi, 0.01)


def g(x):
    return (np.sin(x)) ** 2 - np.cos(x)


fig, ax = plt.subplots()
ax.plot(x, g(x))
ax.set_title(
    "Theoretical Minimum: Interlude 1 - Exercise 1\nGraph of $g(x) = \\sin ^2x - \\cos x$",
    usetex=True,
)
ax.set_xlabel("$x$", usetex=True)
ax.set_ylabel("$g(x)$", usetex=True)

plt.xticks(
    np.arange(-2 * pi, 2 * pi + pi / 2, step=(pi / 2)),
    [
        "$-2\\pi$",
        "$-\\frac{{3\\pi}}{{2}}$",
        "$-\\pi$",
        "$-\\frac{{\\pi}}{{2}}$",
        "0",
        "$\\frac{{\\pi}}{{2}}$",
        "$\\pi$",
        "$\\frac{{3\\pi}}{{2}}$",
        "$2\\pi$",
    ],
    usetex=True,
)

fig.savefig("i01ex01d.png", dpi=300)
