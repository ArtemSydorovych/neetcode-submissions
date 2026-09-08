class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def dfs(r,c):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]

            if r == rows - 1 and c == cols - 1:
                return 1
            
            memo[(r,c)] = dfs(r + 1, c) + dfs(r, c + 1)

            return memo[(r,c)]


        return dfs(0,0)