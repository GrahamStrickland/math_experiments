#!/usr/bin/env python3

def shanks_bot(p: int) -> int:
    """Given a prime number p, return the period of its reciprocal."""
    dividend = 1
    divisor = p
    dividends: list[int] = []

    while len(dividends) < p - 1:
        while divisor > dividend: 
            dividend *= 10

        while divisor + p < dividend:
            divisor += p

        if dividend in dividends:
            break
        else:
            dividends.append(dividend)

        dividend -= divisor
        divisor = p
    
    return len(dividends)
