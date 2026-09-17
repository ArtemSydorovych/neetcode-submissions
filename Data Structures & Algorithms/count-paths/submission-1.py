from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        
        @cache
        def dfs(r,c):
            if r == m -1 and c == n - 1:
                return 1
            if r == rows or c == cols:
                return 0
            res = dfs(r + 1, c) + dfs(r, c + 1)

            return res
        

        return dfs(0,0)