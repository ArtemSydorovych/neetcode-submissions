class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        rows, cols = len(grid), len(grid[0])

        heap = [(grid[0][0], (0,0))]
        dist = {}

        while heap:
            timeToNode, (r,c) = heapq.heappop(heap)

            if (r,c) in dist:
                continue

            dist[(r,c)] = timeToNode

            if r == rows - 1 and c == cols - 1:
                return max(dist.values())
            
            for dr, dc in dirs:
                newR, newC = dr + r, dc + c
                if (newR >= 0 and newR < rows and newC >= 0 and newC < cols):
                    if (newR,newC) not in dist:
                        heapq.heappush(heap, (grid[newR][newC], (newR,newC)))

