#!/usr/bin/env python3

l1 = [0, 1, 2, 0, 3, 4, 5]
counter = 0
for i in l1:
    if i == 0:
        l1.remove(i)
        counter += 1
        
for j in range(counter, 0, -1):
    l1.append(0)
    
# The above code failed for the input [1,0,0]
    
def move_zeros_to_end(arr):
    non_zero_index = 0
    
    # Move non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    
    # Fill the remaining positions with zeros
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
    
    return arr

# Example usage
arr = [0, 1, 2, 0, 3, 4, 5]
print(move_zeros_to_end(arr))  # Output should be [1, 2, 3, 4, 5, 0, 0]

arr = [0, 0, 0, 1, 2, 3]
print(move_zeros_to_end(arr))  # Output should be [1, 2, 3, 0, 0, 0]