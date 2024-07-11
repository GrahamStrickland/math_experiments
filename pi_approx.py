#!/usr/bin/env python3
def pi_approx(n: int) -> float:
    pi = 1.0
    for i in range(1, n):
        sign = -1 if i % 2 != 0 else 1
        pi += sign * (1/(2*i + 1))
    return 4.0 * pi


if __name__ == "__main__":
    n = 2**26
    pi = pi_approx(n)
    print(f"After {n} iterations, pi ~= {pi}")

