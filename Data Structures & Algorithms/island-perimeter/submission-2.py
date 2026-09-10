class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])

        res = 0

        def dfs(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0):
                return 1

            if grid[r][c] == 2:
                return 0    

            grid[r][c] = 2
            size = 0
            for dr, dc in dirs:
                size += dfs(r+dr,c+dc)

            return size

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = dfs(r,c)

        

        return res