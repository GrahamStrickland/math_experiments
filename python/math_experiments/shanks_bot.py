#!/usr/bin/env python3


def shanks_bot(p: int) -> int:
    """Given a prime number p, return the period of its reciprocal."""
    assert p > 1

    remainder = 1
    remainders = {}

    step = 0
    while remainder != 0:
        if remainder in remainders:
            return step - remainders[remainder]

        remainders[remainder] = step

        remainder = (remainder * 10) % p
        step += 1

    return 0
