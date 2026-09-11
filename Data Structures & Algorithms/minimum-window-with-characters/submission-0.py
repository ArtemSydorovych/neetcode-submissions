class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        counts = Counter(t)
        currentWindowCounts = defaultdict(int)
        minSubstr, minLen = [-1, -1], float('inf')
        l = 0
        have, need = 0, len(counts)
        for r, char in enumerate(s):
            
            currentWindowCounts[char] += 1

            if char in counts and currentWindowCounts[char] == counts[char]:
                have += 1 

            while have == need:
                if r - l + 1 < minLen:
                    minSubstr = [l,r]
                    minLen = r - l + 1
            
                currentWindowCounts[s[l]] -= 1
                if s[l] in counts and currentWindowCounts[s[l]] < counts[s[l]]:
                    have -= 1
                l += 1
        
        l, r = minSubstr

        return s[l : r + 1] if minLen != float('inf') else ''