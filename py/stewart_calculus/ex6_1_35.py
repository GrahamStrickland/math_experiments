#!/usr/bin/env python3
import os

import matplotlib.pyplot as plt
import numpy as np


def f(x: float) -> float:
    return abs(np.sqrt(x + 2) - x)


def main() -> None:
    x = np.linspace(0.0, 4.0)

    y = f(x)

    fig = plt.figure()
    plt.plot(x, y)

    plt.show()
    fig.savefig(os.path.join("src", "plots", "stewart_ex6_1_35.pdf"), dpi=300)


if __name__ == "__main__":
    main()
