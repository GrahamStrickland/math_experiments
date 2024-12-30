#!/usr/bin/env python3
import pytest

from src.shanks_bot import shanks_bot


@pytest.mark.parametrize(
    "input, expected",
    [
        (7, 6),
        (23, 20),
        (60013, 5001),
        (60017, 60016),
        (61141, 12228),
        (62057, 62056),
        (61547, 30773),
    ],
)
def test_shanks_bot(input: int, expected: int) -> None:
    assert shanks_bot(input) == expected
