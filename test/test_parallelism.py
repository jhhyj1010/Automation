#!/usr/bin/env python3

import time
import multiprocessing as mp
import concurrent.futures as cf

def f():
    print("function f...")
    time.sleep(3)

def g():
    print("function g...")
    time.sleep(3)

fun_list1 = [f,g]

def exec_fun1(index):
    fun_list1[index]()




fun_list = []

def a():
    print("function a...")
    #pool1 = mp.Pool(mp.cpu_count()*2)
    #results1 = pool1.map(exec_fun1, [i for i in range(len(fun_list1))])
    #pool1.close()
    time.sleep(3)

def b():
    print("function b...")
    time.sleep(3)
    with cf.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())

def c():
    print("function c...")
    time.sleep(3)

def d():
    print("function d...")
    time.sleep(3)

def e():
    print("function e...")
    time.sleep(3)

def h():
    print("function h...")
    time.sleep(3)

def i():
    print("function i...")
    time.sleep(3)

def j():
    print("function j...")
    time.sleep(3)
####


fun_list = [a,b,c,d,e,h,i,j]


#for i in range(len(fun_list)):
#    fun_list[i]()

def exec_fun(index):
    fun_list[index]()

pool = mp.Pool(mp.cpu_count())
results = pool.map(exec_fun, [i for i in range(len(fun_list))])
pool.close()

l1 = [i for i in range(100)]
#print(l1)

l2 = []
while l1:
    l1_subset = l1[:10]
    l1 = l1[10:]
    l2.append(l1_subset)

#print(l2)
l3 = [row for row in l2]
#print(l3)