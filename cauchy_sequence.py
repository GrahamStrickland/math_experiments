#!/usr/bin/env python3

import argparse

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["text.usetex"] = True


def x_n(a: float, b: float, n: int) -> float:
    return ((b - a) / n) + a


def plot_sequence(a: float, b: float, max_n: int) -> None:
    assert a < b and max_n >= 1

    nums = [x_n(a, b, n) for n in range(1, max_n)]

    plt.figure(figsize=(8, 2))
    plt.scatter(nums, [0] * len(nums), color="blue", s=10)
    plt.yticks([])
    plt.xlabel("Values")
    plt.title(
        f"Scatter Plot of Values for the sequence $x_n = \\frac{{{b} - {a}}}{{n}} + {a}$"
    )
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.show()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""
Plot a Caucy sequence over the interval (a, b) where a and b are such that a < b
    """
    )

    parser.add_argument("a", nargs="?", default=None, type=float, help="A float")
    parser.add_argument("b", nargs="?", default=None, type=float, help="A float > a")
    parser.add_argument(
        "max",
        nargs="?",
        default=50,
        type=int,
        help="Maximum number of points to plot",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    plot_sequence(args.a, args.b, args.max)


if __name__ == "__main__":
    main()
