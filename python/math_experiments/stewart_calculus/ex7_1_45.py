#!/usr/bin/env python3
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x: float) -> float:
    return x**3 * np.sqrt(1 + x**2)


def F(x: float) -> float:
    return (1 + x**2) ** (5 / 2) / 5 - (1 + x**2) ** (3 / 2) / 3


def main() -> None:
    x = np.linspace(-2, 2)

    y = f(x)
    i = F(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, "b")
    ax.plot(x, i, "r")

    ax.axis([-2, 2, -2, 2])
    ax.set_title("Stewart Ex. 7.1.45")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.legend(
        (r"$y = x^3 \sqrt{1 + x^2}$", r"$y = \int x^3 \sqrt{1 + x^2} \mathrm{d}x$")
    )
    ax.grid()

    plt.show()
    fig.savefig(
        os.path.join("math_experiments", "plots", "stewart_ex7_1_45.pdf"), dpi=300
    )


if __name__ == "__main__":
    main()
