'''def solution(A):
    max_income = 0
    current_asset_value = 0
    holding = False

    for i in range(len(A)):
        if holding:
            if i == len(A) - 1 or A[i] > A[i + 1]:
                max_income += A[i] - current_asset_value
                holding = False
        else:
            if i < len(A) - 1 and A[i] < A[i + 1]:
                current_asset_value = A[i]
                holding = True

    return max_income % 1000000000
'''

def solution(A):
    max_income, current_asset_value = 0, 0
    holding = False
    import pdb; pdb.set_trace()

    for i in range(len(A)):
        if i == 0:
            if A[i] > A[i+1]:
                #print("111")
                holding = False
                max_income += A[i] - current_asset_value
        else:
            if i < len(A) - 2 and A[i] > A[i-1] and A[i] >= A[i+1]:
                #print("222")
                holding = False
                max_income += A[i] - current_asset_value
            else:
                if holding:
                    if i == len(A) - 1 or A[i] > A[i + 1]:
                        max_income += A[i] - current_asset_value
                        holding = False
                else:
                    if i < len(A) - 1 and A[i] < A[i + 1]:
                        current_asset_value = A[i]
                        holding = True
            '''if i < len(A) - 2 and A[i] > A[i-1] and A[i] >= A[i+1]:
                #print("222")
                holding = False
                max_income += A[i] - current_asset_value'''

        '''if i < len(A) - 1 and A[i] < A[i + 1]:
            print("333")
            current_asset_value = A[i]
            holding = True'''
        '''if holding:
            if i == len(A) - 1 or A[i] > A[i + 1]:
                max_income += A[i] - current_asset_value
                holding = False
        else:
            if i < len(A) - 1 and A[i] < A[i + 1]:
                current_asset_value = A[i]
                holding = True'''

    return max_income % 1000000000

# Example usage:
if __name__ == "__main__":
    A1 = [4, 1, 2, 3]
    print("A1 is: ",solution(A1))  # Output: 6

    A2 = [1, 2, 3, 3, 2, 1, 5]
    print("A2 is: ",solution(A2))  # Output: 7

    A3 = [1000000000, 1, 2, 2, 1000000000, 1, 1000000000]
    print("A3 is: ",solution(A3))  # Output: 999999998
