#!/usr/bin/env python3
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x: float) -> float:
    return np.sin(x) + x**2


def main() -> None:
    x = np.linspace(-np.pi, np.pi)

    fig, ax = plt.subplots()
    ax.plot(x, f(x))
    ax.plot(x, f(x) + 1)
    ax.plot(x, f(x) + 2)
    ax.plot(x, f(x) + 3)
    ax.plot(x, f(x) - 1)
    ax.plot(x, f(x) - 2)
    ax.plot(x, f(x) - 3)

    ax.set_title("Stewart Ex. 5.4.19")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.legend(
        (
            "$y = \\sin x + x^2$",
            "$y = \\sin x + x^2 + 1$",
            "$y = \\sin x + x^2 + 2$",
            "$y = \\sin x + x^2 + 3$",
            "$y = \\sin x + x^2 - 1$",
            "$y = \\sin x + x^2 - 2$",
            "$y = \\sin x + x^2 - 3$",
        )
    )
    ax.grid()

    plt.show()
    fig.savefig(os.path.join("src", "plots", "stewart_ex5_4_19.pdf"), dpi=300)


if __name__ == "__main__":
    main()
