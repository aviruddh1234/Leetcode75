def combinationsum(k, n):
    res = []
    curr = []
    
    def backtrack(i):
        if sum(curr) > n or len(curr) > k:
            return 

        if i>9:
            return 

        if sum(curr) == n and len(curr) == k:
            res.append(curr.copy())
            return 

        curr.append(i)
        backtrack(i + 1)
        
        curr.pop()
        backtrack(i + 1)
    
    backtrack(1)
    return res 

k = int(input("Enter k: "))
n = int(input("Enter n: "))
print(combinationsum(k, n))