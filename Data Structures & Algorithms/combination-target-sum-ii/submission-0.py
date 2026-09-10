class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range (i, len(candidates)):
                if candidates[j] > target - total:
                    break
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                cur.append(candidates[j])
                helper(j + 1, cur, total + candidates[j])
                cur.pop()

        helper(0, [], 0)

        return res