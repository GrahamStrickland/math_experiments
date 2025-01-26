#!/usr/bin/env python3

# Giancoli - Physics: Principles with Applications - Chapter 3, Ex. 3-34
import numpy as np


# define functions for total elapsed time, x-position, and y-position
def t(theta: float, a: float) -> float:
    for i in range(len(a)):
        a[i][0] = i * (((40.0 * np.sin(np.radians(theta))) / 4.90) / 10)


def x(theta: float, a: float) -> float:
    for i in range(len(a)):
        a[i][1] = 40.0 * np.cos(np.radians(theta)) * a[i][0]


def y(theta: float, a: float) -> float:
    for i in range(len(a)):
        a[i][2] = 40.0 * np.sin(np.radians(theta)) * a[i][0] - 4.90 * a[i][0] ** 2


def main() -> None:
    # declare array with angles (theta)
    angles = np.zeros([6])
    for i in range(6):
        angles[i] = 15 * (i + 1)

    # declare array with values for t, x, and y
    data = np.zeros([6, 10, 3])
    for i in range(6):
        t(angles[i], data[i])
        x(angles[i], data[i])
        y(angles[i], data[i])


    # print table of results
    print("=" * 50)
    print("Table of positions for projectile fired at 40.0m/s")
    print("=" * 50, "\n")
    for i in range(6):
        print("Angle = {}{}".format(angles[i], "\N{DEGREE SIGN}"))
        print("-" * 50)
        print("Time Elapsed (s)\tx-position\ty-position")
        print("-" * 50)
        for j in range(10):
            print(
                "{:.6f}\t\t{:.6f}\t{:.6f}".format(
                    data[i][j][0], data[i][j][1], data[i][j][2]
                )
            )
        print("\n")


if __name__ == "__main__":
    main()
