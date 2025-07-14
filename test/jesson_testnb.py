#!/usr/bin/env python3
#from timeit import timeit
import numpy as np
import numba
from numba import jit
from timeit import timeit
def t1():
    x = 0
    for i in np.arange(5000):
        x += i
    return x

#timeit(t1())

@jit(nopython=True)
def t2():
    x = 0
    for i in np.arange(5000):
        x += i
    return x
#timeit(t2())
t2_time = timeit("t2()", number=100, globals=globals())
f"Average time is {t2_time/100:.2f} seconds"
t1_time = timeit("t1()", number=100, globals=globals())
print(t1_time)
print(t2_time)

