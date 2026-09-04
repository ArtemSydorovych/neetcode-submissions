class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            sort = ''.join(sorted(s))
            res[sort] += [s]
        
        return list(res.values())        