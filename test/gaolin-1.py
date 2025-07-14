#!/usr/bin/env python
from memory_profiler import profile

@profile
def two_sum(numbers, target):
    num_to_index = {}
    
    for index, num in enumerate(numbers):
        complement = target - num
        print('complement:', complement)
        if complement in num_to_index: # check if the complement exists in the key of dict
            print('complement matched:', complement)
            return [num_to_index[complement], index]
        num_to_index[num] = index
        print('num_to_index:', num_to_index)

# Example usage
numbers = [1, -2, 3, 10, -4, 7, 2, -5]
target = 17
result = two_sum(numbers, target)
print(result)  # Output should be [3, 4] since numbers[3] + numbers[4] = 10 + 7 = 17
