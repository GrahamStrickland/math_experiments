#!/usr/bin/env python3

# Classical Mechanics: The Theoretical Minimum - Leonard Susskind & George Hrabovsky
# Interlude 1: Exercise 8 (d)

from typing import Tuple

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.rcParams["text.usetex"] = True


# Function for position
def r(t: float, c: float) -> Tuple[float]:
    return (c * (t - np.sin(t)), c * (1 - np.cos(t)))


# Function for velocity
def v(t: float, c: float) -> Tuple[float]:
    return (c * (1 - np.cos(t)), c * np.sin(t))


# Function for acceleration
def a(t: float, c: float) -> Tuple[float]:
    return (c * np.sin(t), c * np.cos(t))


def main() -> None:
    t = np.linspace(-2 * np.pi, 2 * np.pi, 100)

    ax = plt.figure().add_subplot(projection="3d")
    z = t
    c = 2
    ax.plot(r(z, c)[0], r(z, c)[1], z)
    ax.plot(v(z, c)[0], v(z, c)[1], z)
    ax.plot(a(z, c)[0], a(z, c)[1], z)
    ax.set_title("Theoretical Minimum: Interlude 1 - Exercise 8 (d)\n($c = 2$)")
    ax.legend(
        [
            r"$\vec{r} = \bigl(c(t - \sin t), c(1 - \cos t)\bigr)$",
            r"$\vec{v} = \bigl(c(1 - \cos t), c\sin t\bigr)$",
            r"$\vec{a} = (c\sin t, c\cos t)$",
        ]
    )

    plt.show()


if __name__ == "__main__":
    main()
