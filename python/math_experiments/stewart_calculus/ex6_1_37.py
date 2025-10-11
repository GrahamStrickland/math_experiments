#!/usr/bin/env python3
import os

import matplotlib.pyplot as plt
import numpy as np


def f(x: float) -> float:
    return x * np.sin(x**2)


def main() -> None:
    x = np.linspace(0.0, 4.0)

    y = f(x)

    fig = plt.figure()
    plt.plot(x, y)

    plt.show()
    fig.savefig(
        os.path.join("math_experiments", "plots", "stewart_ex6_1_37.pdf"), dpi=300
    )


if __name__ == "__main__":
    main()
