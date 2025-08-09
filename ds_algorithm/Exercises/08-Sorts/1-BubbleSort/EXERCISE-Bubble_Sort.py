## WRITE BUBBLE_SORT FUNCTION HERE ##
#                                   #
#                                   #
#                                   #
#                                   #
#####################################
def bubble_sort(nums):
    for i in range(0, len(nums)-1):
        for j in range(1+i, len(nums)):
            if nums[i] > nums[j]:
                '''temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp'''
                nums[i], nums[j] = nums[j], nums[i]

    return nums





print(bubble_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """