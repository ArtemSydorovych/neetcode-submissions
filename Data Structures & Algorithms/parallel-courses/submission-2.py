class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph, indegree = defaultdict(list), [0] * (n + 1)
        
        for a,b in relations:
            graph[a].append(b)
            indegree[b] += 1

        q = deque(i for i in range(1, n + 1) if indegree[i] == 0)
        
        res = 0
        visited = 0
        while q:
            for i in range(len(q)):
                course = q.popleft()
                visited += 1 
                for neigh in graph[course]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            
            res += 1



        return res if visited == n else -1