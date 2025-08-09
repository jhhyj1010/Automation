def produce_multiply_except_self(nums: list) -> list:
    """
        Space complexity: O(2N)
        Time complexity: O(N)
    """
    length = len(nums)
    #L = R = answers = [0]*length # L,R,answers are exactly same object with same addresses
    L, R, answers = [0]*length,[0]*length,[0]*length # L, R and answers are different objects with different addresses

    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i-1]*L[i-1]

    R[length-1] = 1
    for j in reversed(range(length-1)):
        R[j] = nums[j+1]*R[j+1]

    for k in range(length):
        answers[k] = L[k]*R[k]
    
    print("Left values:", L)
    print("Right values:", R)
    return answers

nums = [4,5,1,8,2]
print(produce_multiply_except_self(nums))
