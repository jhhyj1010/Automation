def subarray_sum(nums, target):
    # Dictionary to store cumulative sum and its earliest index
    sum_indices = {0: -1}
    curr_sum = 0

    for i, num in enumerate(nums):
        curr_sum += num
        if (curr_sum - target) in sum_indices:
            # Return the start and end indices of the subarray
            return (sum_indices[curr_sum - target] + 1, i)
        sum_indices[curr_sum] = i
    return None  # No subarray found

nums = [1, 2, 3, 7, 5]
target = 12
print(subarray_sum(nums, target))  # Output: (2, 4)  # nums[2:5] = [3, 7,