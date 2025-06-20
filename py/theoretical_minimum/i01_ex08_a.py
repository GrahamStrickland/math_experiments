#!/usr/bin/env python3

# Classical Mechanics: The Theoretical Minimum - Leonard Susskind & George Hrabovsky
# Interlude 1: Exercise 8 (a)

from typing import Tuple

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.rcParams["text.usetex"] = True


# Function for position
def r(t: float, omega: float) -> Tuple[float]:
    return (np.cos(omega * t), np.exp(omega * t))


# Function for velocity
def v(t: float, omega: float) -> Tuple[float]:
    return (-omega * np.sin(omega * t), omega * np.exp(omega * t))


# Function for acceleration
def a(t: float, omega: float) -> Tuple[float]:
    return (-(omega**2) * np.cos(omega * t), omega**2 * np.exp(omega * t))


def main() -> None:
    t = np.linspace(-2 * np.pi, 2 * np.pi, 100)

    ax = plt.figure().add_subplot(projection="3d")
    z = t
    omega = 0.5
    ax.plot(r(z, omega)[0], r(z, omega)[1], z)
    ax.plot(v(z, omega)[0], v(z, omega)[1], z)
    ax.plot(a(z, omega)[0], a(z, omega)[1], z)
    ax.set_title("Theoretical Minimum: Interlude 1 - Exercise 8 (a)\n($\\omega = 0.5$)")
    ax.legend(
        [
            r"$\vec{r} = (\cos \omega t, e^{\omega t})$",
            r"$\vec{v} = (-\omega \sin \omega t, \omega e^{\omega t})$",
            r"$\vec{a} = (-\omega^2 \cos \omega t, \omega^2 e^{\omega t})$",
        ]
    )

    plt.show()


if __name__ == "__main__":
    main()
