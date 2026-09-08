from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dfs(i):
            if (i >= len(cost)):
                return 0
            
            return min(dfs(i + 2) + cost[i], dfs(i + 1) + cost[i])
    

        return min(dfs(0), dfs(1))  