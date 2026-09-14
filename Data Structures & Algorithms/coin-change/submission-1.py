from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(target):
            if target == 0:
                return 0
            res = float('inf')

            for coin in coins:
                if target - coin >= 0:
                    res = min(res, 1 + dfs(target - coin))

            return res

        
        minCoins = dfs(amount)
        return -1 if minCoins == float('inf') else minCoins