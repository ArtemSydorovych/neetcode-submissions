class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        curSet = set()
        l = 0

        for r, char in enumerate(s):
            
            while char in curSet and l < r:
                curSet.remove(s[l])
                l += 1
            
            curSet.add(char)

            maxLen = max(len(curSet), maxLen)
        

        return maxLen