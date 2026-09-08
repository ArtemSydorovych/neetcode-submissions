from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            total = 0

            if (i >= len(s)):
                return 1
            
            if s[i] != '0':
               total += dfs(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                total += dfs(i + 2)

            return total
        

        return dfs(0)


