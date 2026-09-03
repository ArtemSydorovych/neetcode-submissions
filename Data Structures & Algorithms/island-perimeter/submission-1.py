class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(r, c):
            if(r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0):
                return 1

            if (grid[r][c] == 2):
                return 0

            grid[r][c] = 2
            perim = 0
            for (dr, dc) in DIRECTIONS:
                perim += dfs(r + dr, c + dc)

            return perim

        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c]):
                    return dfs(r,c)

        return 0