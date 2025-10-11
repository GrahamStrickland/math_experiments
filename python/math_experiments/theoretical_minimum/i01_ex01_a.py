#!/usr/bin/env python3

# Classical Mechanics: The Theoretical Minimum - Leonard Susskind & George Hrabovsky
# Interlude 1: Exercise 1 (a)

import os

import matplotlib.pyplot as plt
import numpy as np


def f(t: float) -> float:
    return t**4 + 3 * t**3 - 12 * t**2 + t - 6


def main() -> None:
    t = np.arange(-8, 8, 0.1)

    fig, ax = plt.subplots()
    ax.plot(t, f(t))
    ax.set_title(
        "Theoretical Minimum: Interlude 1 - Exercise 1\nGraph of $f(t) = t^4 + 3t^3 - 12t^2 + t - 6$",
        usetex=True,
    )
    ax.set_xlabel("$t$", usetex=True)
    ax.set_ylabel("$f(t)$", usetex=True)

    plt.show()
    fig.savefig(os.path.join("math_experiments", "plots", "tm_i01_ex01_a.pdf"), dpi=300)


if __name__ == "__main__":
    main()
