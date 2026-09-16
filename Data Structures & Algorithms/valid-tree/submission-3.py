class UF:
    def __init__(self, n):
        self.par = {}
        self.size = {}
        self.count = 0
        
        for x in range(n):
            self.par[x] = x
            self.size[x] = 1
            self.count += 1

    def find(self, n):
        cur = n

        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]

        return cur
    
    def union(self, n1, n2):
        f1, f2 = self.find(n1), self.find(n2)

        if f1 == f2:
            return False
        
        if self.size[f1] < self.size[f2]:
            f1,f2 = f2,f1

        self.par[f2] = f1
        self.size[f1] += self.size[f2]
        self.count -= 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = UF(n)

        for u,v in edges:
            if not dsu.union(u,v):
                return False
        
        print(dsu.count)
        return dsu.count == 1
