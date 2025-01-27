#!/usr/bin/env python3

# Classical Mechanics: The Theoretical Minimum - Leonard Susskind & George Hrabovsky
# Interlude 1: Exercise 8 (c)

from typing import Tuple

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.rcParams["text.usetex"] = True


# Function for position
def r(t: float, c: float) -> Tuple[float]:
    return (c * np.cos(t) ** 3, c * np.sin(t) ** 3)


# Function for velocity
def v(t: float, c: float) -> Tuple[float]:
    return (-3 * c * np.sin(t) ** 2 * np.cos(t), 3 * c * np.cos(t) ** 2 * np.sin(t))


# Function for acceleration
def a(t: float, c: float) -> Tuple[float]:
    return (
        -3 * c * (2 * np.cos(t) ** 2 * np.sin(t) - np.sin(t) ** 3),
        3 * c * (-2 * np.sin(t) ** 2 * np.cos(t) + np.cos(t) ** 3),
    )


def main() -> None:
    t = np.linspace(-2 * np.pi, 2 * np.pi, 100)

    ax = plt.figure().add_subplot(projection="3d")
    z = t
    c = 2
    ax.plot(r(z, c)[0], r(z, c)[1], z)
    ax.plot(v(z, c)[0], v(z, c)[1], z)
    ax.plot(a(z, c)[0], a(z, c)[1], z)
    ax.set_title("Theoretical Minimum: Interlude 1 - Exercise 8 (c)\n($c = 2$)")
    ax.legend(
        [
            r"$\vec{r} = (c\cos^3 t, c\sin^3 t)$",
            r"$\vec{v} = (-3c\sin^2 t \cos t, 3c\cos^2 t \sin t)$",
            r"$\vec{a} = \bigl(-3c(2\cos^2 t \sin t - \sin^3 t), -3c(2\sin^2 t \cos t - \cos^3 t)\bigr)$",
        ]
    )

    plt.show()


if __name__ == "__main__":
    main()
