class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            power = mid * mid 
            if power > x:
                r = mid - 1
            elif power < x:
                l = mid + 1
                res = mid 
            else:
                return mid
            

        return res