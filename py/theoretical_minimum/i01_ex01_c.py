#!/usr/bin/env python3

# Classical Mechanics: The Theoretical Minimum - Leonard Susskind & George Hrabovsky
# Interlude 1: Exercise 1 (b)

import os

import matplotlib.pyplot as plt
import numpy as np


def theta(alpha: float) -> float:
    return np.exp(alpha) + alpha * np.log(alpha)


def main() -> None:
    a = np.arange(0.5, 5.5, 0.1)

    fig, ax = plt.subplots()
    ax.plot(a, theta(a))
    ax.set_title(
        "Theoretical Minimum: Interlude 1 - Exercise 1\nGraph of $\\theta(\\alpha) = e^\\alpha + \\alpha ln(\\alpha) $",
        usetex=True,
    )
    ax.set_xlabel("$\\alpha$", usetex=True)
    ax.set_ylabel("$\\theta(\\alpha)$", usetex=True)

    plt.show()
    fig.savefig(os.path.join("src", "plots", "tm_i01_ex01_c.pdf"), dpi=300)


if __name__ == "__main__":
    main()
