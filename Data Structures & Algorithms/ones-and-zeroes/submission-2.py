from functools import cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        @cache
        def dfs(i, totalZeroes, totalOnes):
            if i >= len(strs):
                return 0

            res = dfs(i + 1, totalZeroes, totalOnes)

            c0, c1 = count(strs[i])

            if totalZeroes >= c0 and totalOnes >= c1:
                res = max(res, 1 + dfs(i + 1, totalZeroes - c0, totalOnes - c1))
        
            return res

        @cache
        def count(s):
            zeroes = 0
            ones = 0
            for char in s:
                if char == "0":
                    zeroes += 1
                if char == "1":
                    ones += 1

            return (zeroes, ones)

        return dfs(0, m, n)
