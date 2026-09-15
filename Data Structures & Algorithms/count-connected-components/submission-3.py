class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    
    def find(self, n):
        cur = n
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]

        return cur

    def union(self, n1, n2): 
        node1, node2 = self.find(n1), self.find(n2)

        if node1 == node2:
            return False
        if self.rank[node1] > self.rank[node2]:
            node1, node2 = node2, node1

        self.par[node2] = node1
        self.rank[node1] += self.rank[node2]
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        res = n
        for u, v in edges:
            if unionFind.union(u,v):
                res -= 1
        
        return res