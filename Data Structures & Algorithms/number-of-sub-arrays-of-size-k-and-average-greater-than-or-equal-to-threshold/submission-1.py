class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        l = 0
        res = 0
        curSum = 0

        for r in range(len(arr)):
            curSum += arr[r]
            
            while (r - l + 1 > k):
                curSum -= arr[l]
                l+=1
            

            if curSum >= threshold and r - l + 1 == k:
                res += 1

        return res