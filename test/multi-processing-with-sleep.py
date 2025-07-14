#!/usr/bin/env python

# create a program with multiprocessing
# to calculate the sum of the first 1000 numbers

import multiprocessing
import time

def print_log(msg):
    time.sleep(1)
    print(msg)
    
with multiprocessing.Pool(16) as p:
    p.map(print_log, range(100))

print("Done!")