
def permute(input_list: list) -> list:
    length = len(input_list)
    ans, sol = [], []

    def backtrack():
        if len(sol) == length:
            print("returning sol is --- ", sol)
            ans.append(sol[:]) # Copy sol instead operating in-place
            return
        for i in input_list:
            if i not in sol:
                print("adding ", i)
                sol.append(i)
                backtrack()
                print("i is ", i, "sol is ", sol)
                print("Poping ",sol.pop())
    
    backtrack()
    return ans


l1 = [1,2,3]
print(permute(l1))