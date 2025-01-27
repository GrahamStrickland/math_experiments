#!/usr/bin/env python3

# Classical Mechanics: The Theoretical Minimum - Leonard Susskind & George Hrabovsky
# Interlude 1: Exercise 8 (b)

from typing import Tuple

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.rcParams["text.usetex"] = True


# Function for position
def r(t: float, omega: float, phi: float) -> Tuple[float]:
    return (np.cos(omega * t - phi), np.sin(omega * t - phi))


# Function for velocity
def v(t: float, omega: float, phi: float) -> Tuple[float]:
    return (-omega * np.sin(omega * t - phi), omega * np.cos(omega * t - phi))


# Function for acceleration
def a(t: float, omega: float, phi: float) -> Tuple[float]:
    return (-(omega**2) * np.cos(omega * t - phi), -(omega**2) * np.cos(omega * t))


def main() -> None:
    t = np.linspace(-2 * np.pi, 2 * np.pi, 100)

    ax = plt.figure().add_subplot(projection="3d")
    z = t
    omega = 0.5
    phi = 0.25
    ax.plot(r(z, omega, phi)[0], r(z, omega, phi)[1], z)
    ax.plot(v(z, omega, phi)[0], v(z, omega, phi)[1], z)
    ax.plot(a(z, omega, phi)[0], a(z, omega, phi)[1], z)
    ax.set_title(
        "Theoretical Minimum: Interlude 1 - Exercise 8 (b)\n($\\omega = 0.5, \\phi = 0.25$)"
    )
    ax.legend(
        [
            r"$\vec{r} = \bigl(\cos (\omega t - \phi), \sin (\omega t - \phi\bigr)$",
            r"$\vec{v} = \bigl(-\omega \sin (\omega t - phi), \omega \cos (\omega t - \phi) \bigr)$",
            r"$\vec{a} = \bigl(-\omega^2 \cos (\omega t - \phi), -\omega^2 \sin(\omega t - \phi) \bigr)$",
        ]
    )

    plt.show()


if __name__ == "__main__":
    main()
