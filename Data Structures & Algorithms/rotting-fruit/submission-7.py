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
                if grid[r][c] == 1:
                    countFresh += 1

        
        while q and countFresh > 0:        
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    newR, newC = dr + r, c + dc

                    if (newR >= 0 and newR < rows and newC >= 0 and newC < cols and grid[newR][newC] == 1):         
                        grid[newR][newC] = 2
                        countFresh -= 1
                        q.append((newR,newC))
                
            res += 1
            


        print(countFresh)
        return res if countFresh == 0 else -1