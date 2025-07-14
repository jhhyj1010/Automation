#!/usr/bin/env python3
import numpy as np
import numba 
from numba import jit

@jit(nopython=True)
def go_fast(a):
    trace = 0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace 

x = np.arange(100).reshape(10, 10)
