class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        countFresh = 0

        q = deque()

        # fill queue with rotten (as we start from them)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    countFresh += 1

        minutesPassed = 0
        while q and countFresh > 0:
            
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc

                    if (newR >= 0 and newR < rows and newC >= 0 and newC < cols and grid[newR][newC] == 1):
                        print(newR )
                        print(newC)
                        grid[newR][newC] = 2
                        countFresh -= 1
                        q.append((newR,newC))
                
            minutesPassed += 1

            

        return minutesPassed if countFresh == 0 else -1