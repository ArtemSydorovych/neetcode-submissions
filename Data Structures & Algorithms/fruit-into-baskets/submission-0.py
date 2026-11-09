class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = defaultdict(int)
        l = 0

        for r in range(len(fruits)):
            types[fruits[r]] += 1

            if len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    types.pop(fruits[l])
                l+= 1
        

        return len(fruits) - l
