class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        res = 0
        l = 0
        currentSet = set()

        for r, char in enumerate(s):

            while(char in currentSet):
                currentSet.remove(s[l])
                l+=1

            currentSet.add(char)
            res = max(res, r - l + 1)

        return res;
