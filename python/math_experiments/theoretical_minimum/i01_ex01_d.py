#!/usr/bin/env python3

# Classical Mechanics: The Theoretical Minimum - Leonard Susskind & George Hrabovsky
# Interlude 1: Exercise 1 (d)

import os

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi as pi


def g(x: float) -> float:
    return (np.sin(x)) ** 2 - np.cos(x)


def main() -> None:
    x = np.arange(-2 * pi, 2 * pi, 0.01)

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

    plt.show()
    fig.savefig(os.path.join("math_experiments", "plots", "tm_i01_ex01_d.pdf"), dpi=300)


if __name__ == "__main__":
    main()
