class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            ai = (a >> i) & 1
            bi = (b >> i) & 1
            ci = (c >> i) & 1
            if (ai | bi) != ci:
                if ci == 1: ans += 1
                else: ans += ai + bi
        return ans