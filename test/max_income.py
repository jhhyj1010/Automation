def solution(A):
    MOD = 10**9
    max_income = 0
    init_count = 0
    holding = False
    current_asset_value = 0
    
    for i in range(len(A)):
        if holding:
            if i == len(A) - 1 or A[i] > A[i + 1]:
                max_income += A[i] - current_asset_value
                holding = False
        else:
            if i < len(A) - 1:
                if A[i] < A[i + 1] and init_count != 0:
                    current_asset_value = A[i]
                    holding = True
                if A[i] >= A[i + 1] and A[i] > A[i-1]:
                    max_income += A[i] - current_asset_value
                    holding = False
                    init_count += 1
            
    return max_income % MOD

A1 = [4,1,2,3]
A2 = [1,2,3,3,2,1,5]
A3 = [1000000000, 1, 2, 2, 1000000000, 1, 1000000000]
print("A1 is: ",solution(A1))  # Output: 6
print("A2 is: ",solution(A2))  # Output: 6
print("A3 is: ",solution(A3))  # Output: 6