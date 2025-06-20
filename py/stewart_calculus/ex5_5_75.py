#!/usr/bin/env python3
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["text.usetex"] = True


def f(x: float) -> float:
    return np.sqrt(2 * x + 1)


def main() -> None:
    x = np.linspace(0, 1, 100)

    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, "b", label="$y = \\sqrt{{2x + 1}}$")

    ax.axis([0, 1, 0, 2])
    ax.set_title("Stewart Ex. 5.5.75")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.legend()
    ax.grid()

    plt.show()
    fig.savefig(os.path.join("src", "plots", "stewart_ex5_5_75.pdf"), dpi=300)


if __name__ == "__main__":
    main()
