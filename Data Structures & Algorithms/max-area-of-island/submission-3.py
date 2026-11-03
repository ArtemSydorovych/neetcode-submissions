class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]


        def dfs(r,c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2

            area = 1

            for dr, dc in dirs:
                area += dfs(dr + r, dc + c)
            

            return area

        m = 0
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == 1:
                    m = max(m, dfs(r,c))
        
        return m