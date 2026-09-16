class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = 0
        adjList = {}
        indegree = [0] * numCourses

        for i in range(numCourses):
            adjList[i] = []

        for course, prerq in prerequisites:
            adjList[prerq].append(course)
            indegree[course] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            

        while q:
            cur = q.popleft()
            visited += 1
            for nei in adjList[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                



        return visited == numCourses