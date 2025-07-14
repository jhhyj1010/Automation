#!/usr/bin/env python3

import concurrent.futures as cf

def test(n):
    print(2*n)

def test_1(i,j):
    print(2*i)
    print(3*j)

with cf.ProcessPoolExecutor(max_workers=1) as executor:
    #executor.map(test,(1,2,3,4,5,6,7,8))
    executor.map(test_1, [(1,2),(3,4),(5,6)])
