class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS:
                        if grid[newR][newC] == INF:
                            grid[newR][newC] = grid[r][c] + 1
                            q.append((newR, newC))