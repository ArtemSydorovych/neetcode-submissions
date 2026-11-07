class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        rows, cols = len(grid), len(grid[0])
        countFresh = 0
        res = 0

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    countFresh += 1
        

        while q and countFresh > 0:
            
            for _ in range(len(q)):
                (r,c) = q.popleft()
                
                for dr, dc in dirs:
                    nR, nC = dr + r, dc + c
                    if nR >= 0 and nR < rows and nC >= 0 and nC  < cols and grid[nR][nC] == 1:
                        countFresh -= 1
                        grid[nR][nC] = 2
                        q.append((nR,nC))

            res += 1

        return res if countFresh == 0 else -1



