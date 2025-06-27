class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)

        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                a,b = stack.pop()
                res[a] = i-a

            stack.append((i,n))
        
        return res