#!/usr/bin/env python3
print("hello")
from inspect import getgeneratorstate as gs
import pdb

def simple_coro2(a):
    #pdb.set_trace()
    print('-> Started: a =', a)
    b = yield a
    print('Jesson b is ', b)
    print('-> Received: b =', b) # 28
    d = yield a + b
    print('Jesson a+b is ', a+b)
    print('-> Received: d =', d) # 99

    e = yield d - b
    print('Jesson d-b is: ', d-a) # d-a=85
    print('-> Received: e =', e) # 100

#pdb.set_trace()
my_coro2 = simple_coro2(14)
print(gs(my_coro2)) # Started
next(my_coro2) # start the coroutine
print(gs(my_coro2)) # Suspended
my_coro2.send(28) # b is 28 now
print(gs(my_coro2)) # Suspended
my_coro2.send(99) # a+b is 42
print(gs(my_coro2))

my_coro2.send(100)
