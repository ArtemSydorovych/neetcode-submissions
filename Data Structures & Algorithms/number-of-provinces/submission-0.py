class UnionFind:
    def __init__(self, nodes):
        self.par = {}
        self.size = {}
        self.count = len(nodes)

        for n in nodes:
            self.par[n] = n
            self.size[n] = 1
    
    def find(self, node):
        cur = node

        while self.par[cur] != cur:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        
        return cur

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)

        if r1 == r2:
            return False
        elif self.size[r1] < self.size[r2]:
            r1, r2 = r2, r1

        self.par[r2] = r1
        

        self.size[r1] += self.size[r2]
        
        self.count -= 1
        return True


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(range(n))

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    dsu.union(i, j)
        
        return dsu.count