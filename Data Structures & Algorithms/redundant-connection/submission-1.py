class UnionFind:
    
    def __init__(self, edges):
        self.par = {}
        self.rank = {}

        for u, v in edges:
            self.par[v] = v
            self.par[u] = u
            self.rank[v] = 0
            self.rank[u] = 0
    
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
        
        if self.rank[node1] < self.rank[node2]:
            node1, node2 = node2, node1
        
        self.par[node2] = node1
        self.rank[node1] += 1
    
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(edges)

        for u, v in edges:
            if not dsu.union(u,v):
                return [u,v]
        

        return []
