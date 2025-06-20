#!/usr/bin/env python3
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x: float) -> float:
    return x * np.exp(-2 * x)


def F(x: float) -> float:
    return (-x / 2) * np.exp(-2 * x) - (1 / 4) * np.exp(-2 * x)


def main() -> None:
    x = np.linspace(-2, 4)

    y = f(x)
    i = F(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, "b")
    ax.plot(x, i, "r")

    ax.axis([-2, 4, -2, 2])
    ax.set_title("Stewart Ex. 7.1.43")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.legend((r"$y = xe^{-2x}$", r"$y = \int xe^{-2x} \mathrm{d}x$"))
    ax.grid()

    plt.show()
    fig.savefig(os.path.join("src", "plots", "stewart_ex7_1_43.pdf"), dpi=300)


if __name__ == "__main__":
    main()
