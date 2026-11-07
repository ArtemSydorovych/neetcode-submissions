class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = 0
        adjList = defaultdict(list)
        indegree = [0] * numCourses
    
        for a, b in prerequisites:
            adjList[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        while q:
            course = q.popleft()
            visited += 1
            for n in adjList[course]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)


        return visited == numCourses