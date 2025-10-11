#!/usr/bin/env python3
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x: float) -> float:
    return x * (x**2 - 1) ** 3


def F(x: float) -> float:
    return (x**2 - 1) ** 4 / 8


def main() -> None:
    x = np.linspace(-2, 2, 100)

    y = f(x)
    w = F(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, "b", label="$f(x) = x(x^2 - 1)^3$")
    ax.plot(x, w, "r", label="$F(x) = \\frac{{(x^2 - 1)^4}}{{8}}$")

    ax.axis([-2, 2, -2, 2])
    ax.set_title("Stewart Ex. 5.5.49")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.legend()
    ax.grid()

    plt.show()
    fig.savefig(
        os.path.join("math_experiments", "plots", "stewart_ex5_5_49.pdf"), dpi=300
    )


if __name__ == "__main__":
    main()
