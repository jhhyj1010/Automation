#!/usr/bin/env python3

def test(a: str, b: str):
    print(a,b)

t1 = ('a','b')
t2 = ['a', 'c']

test(*t2)