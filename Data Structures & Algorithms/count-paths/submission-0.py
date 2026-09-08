from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        
        @cache
        def dfs(r,c):
            if r == rows or c == cols:
                return 0
            
            if r == rows - 1 and c == cols - 1:
                return 1

            return dfs(r + 1, c) + dfs(r, c + 1)
        

        return dfs(0,0)