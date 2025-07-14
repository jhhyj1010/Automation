#!/usr/bin/env python3
import typing

"""
Plan
Convert List to Set: Convert the list to a set to allow O(1) average time complexity for lookups.
Initialize Variables: Initialize a variable to keep track of the longest sequence length.
Iterate Through the Set: For each element in the set:
Check if it is the start of a sequence (i.e., the previous element is not in the set).
If it is the start, iterate through the sequence to find its length.
Update the longest sequence length if the current sequence is longer.
Return Result: Return the length of the longest continuous sequence.
"""
def longest_continuous_sequence(nums: typing.List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    longest_length = 0

    for num in num_set:
        if num - 1 not in num_set:  # Check if it's the start of a sequence
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest_length = max(longest_length, current_length)

    return longest_length

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longest_continuous_sequence(nums))  # Output should be 4 (sequence: 1, 2, 3, 4)

nums = [0, -1, 1, 2, -2, -3, 3, 4]
print(longest_continuous_sequence(nums))  # Output should be 8 (sequence: -3, -2, -1, 0, 1, 2, 3, 4)