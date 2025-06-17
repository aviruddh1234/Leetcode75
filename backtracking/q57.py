def lettercombinations(digits):
    res = [] 
    curr = []
    
    digitchar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
            }

    def backtrack(i):
        if len(curr) == len(digits):
            res.append(''.join(curr))
            return 

        for char in digitchar[digits[i]]:
            curr.append(char)
            backtrack(i + 1)
            curr.pop()
    

    if digits:
        backtrack(0)
    return res

digits = input()
print(lettercombinations(digits))