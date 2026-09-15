class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # expand until abs(x - curMax) is decreasing or k is reached 
        #(if reached try next item and decide if we leave left or right (if x - right < x - left)) go on, else we've found an answer
        # whne started increasing move left and 

        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]