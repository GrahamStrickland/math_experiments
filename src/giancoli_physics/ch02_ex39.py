#!/usr/bin/env python3
import os

import matplotlib.pyplot as plt
import numpy as np


# Velocity function
def v(t: float, v0: float) -> float:
    return v0 + 9.80 * t


# Distance function
def x(t: float, x0: float, v0: float) -> float:
    return x0 + v0 * t + 0.5 * 9.80 * t**2


def main() -> None:
    # Time intervals between 0.00 and 5.00.
    t = np.linspace(0.00, 5.00, 21)

    # Assign function values over time interval.
    speed = v(t, 0.00)
    distance = x(t, 0.00, 0.00)
    print("Table of values for v(t) and x(t) over 0.00 to 5.00 with intervals of 0.25:")
    print("-" * 44)
    print("Time (s)\tSpeed (m/s)\tDistance (m)")
    print("-" * 44)
    for i in range(21):
        print("{:.2f}\t\t{:.2f}\t\t{:.2f}".format(t[i], speed[i], distance[i]))

    # Plot figures on separate axes.
    fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)
    fig.suptitle("Giancoli - Chapter 2, Ex. 39")

    # Plot speed function.
    ax1.plot(t, speed, "r", label="Speed")
    ax1.set_title("(a)")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Speed (m/s)")

    # Plot distance function.
    ax2.plot(t, distance, "b", label="Distance")
    ax2.set_title("(b)")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Distance (m)")

    # Show and save figure.
    plt.show()
    fig.savefig(
        os.path.join("src", "giancoli_physics", "plots", "ch02_ex39.pdf"), dpi=300
    )


if __name__ == "__main__":
    main()
