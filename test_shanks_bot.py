#!/usr/bin/env python3

from shanks_bot import shanks_bot


def test_shanks_bot() -> None:
    p = 7
    obs = shanks_bot(p)
    actual = 6
    
    assert obs == actual


def test_shanks_bot2() -> None:
    p = 23
    obs = shanks_bot(p)
    actual = 20
    
    assert obs == actual


def test_shanks_bot3() -> None:
    p = 60013
    obs = shanks_bot(p)
    actual = 5001
    
    assert obs == actual


def test_shanks_bot4() -> None:
    p = 60017
    obs = shanks_bot(p)
    actual = 60016
    
    assert obs == actual


def test_shanks_bot5() -> None:
    p = 61141
    obs = shanks_bot(p)
    actual = 12228
    
    assert obs == actual


def test_shanks_bot6() -> None:
    p = 62057
    obs = shanks_bot(p)
    actual = 62056
    
    assert obs == actual


def test_shanks_bot7() -> None:
    p = 61547
    obs = shanks_bot(p)
    actual = 30773
    
    assert obs == actual
