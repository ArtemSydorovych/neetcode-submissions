from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @cache
        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return float('inf')
            

            return min(grid[r][c] + dfs(r + 1,c), grid[r][c] + dfs(r,c + 1))

        return dfs(0,0)