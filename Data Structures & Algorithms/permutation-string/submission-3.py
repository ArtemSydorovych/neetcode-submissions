class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = Counter(s1)
        s2Freq = Counter()

        left = 0;

        for right in range(len(s2)):
            s2Freq[s2[right]] += 1

            if (right - left + 1 > len(s1)):
                
                ## move left 
                s2Freq[s2[left]] -= 1
                if (s2Freq[s2[left]] == 0):
                    del s2Freq[s2[left]]
                left += 1 
                
            
            if s1Freq == s2Freq:
                return True


        return False