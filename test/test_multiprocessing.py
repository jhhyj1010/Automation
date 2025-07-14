#!/usr/bin/env python3
import time
import multiprocessing as mp

def test(n):
    print("in test %d",n)

def test_1(i):
    print(type(i))
    print(*i)
    print(i[0])
    print(i[1])

input = (1,2,3,4,5)
with mp.Pool(processes=4) as pool:
    #res = pool.apply_async(test, (1,))
    #print(res.get(timeout=1))
    #pool.map(test, (1,2,3))
    #pool.map_async(test, (1,2,3))
    res = []
    for i in input:
        print(i)
        r1 = pool.apply_async(test,(i,))
        res.append(r1)
    for i in res:
        i.get() # with get() called, test(n) will be called actually

l1 = [i for i in range(50)]
with mp.Pool(processes=16) as pool:
    ret = pool.imap_unordered(test, l1, chunksize=16)
    for i in ret:
        pass

l2 = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)]
with mp.Pool(processes=16) as pool:
    ret = pool.imap_unordered(test_1, l2, chunksize=16)
    for i in ret:
        pass

