class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []
        res = []

        def helper(i, current):            
            if (len(current) == k):
                res.append(current.copy())
                return

            if i > n:
                return

            current.append(i)
            helper(i + 1, current)
            current.pop()


            helper(i + 1, current)
        
        helper(1, current)

        return res