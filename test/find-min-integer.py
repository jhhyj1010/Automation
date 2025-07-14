#!/usr/bin/env python

print("This is a program for finding out the minimum integer which does not belong to a given array")

def find_min_positive(A):
    simple_array = sorted(list(set(A)))
    min_num = simple_array[0]
    max_num = simple_array[-1]

    if max_num <= 0 or min_num > 1:
        return 1

    # Iterate the array to find the minimum number
    for i in range(min_num, max_num+1):
        if i in simple_array:
            continue
        if i > 0:
            return i

    return max_num + 1


a1 = [-1,-1,-2,-3]
a2 = [-1,-5,1,3,0,1,3]
a3 = [0,1,2,2,3]
a4 = [2,4,5,7,8,9,5,2,90]
print("Input array is: ", a1, " Return value is: ", find_min_positive(a1))
print("Input array is: ", a2, " Return value is: ", find_min_positive(a2))
print("Input array is: ", a3, " Return value is: ", find_min_positive(a3))
print("Input array is: ", a4, " Return value is: ", find_min_positive(a4))

