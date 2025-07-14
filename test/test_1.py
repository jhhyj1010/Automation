#!/usr/bin/env python3

flag = True
l1 = [1,2]
for i in l1:
    if i == 2:
        print("branch 1")
    else:
        flag=False
        print("branch 2")
print(flag)
