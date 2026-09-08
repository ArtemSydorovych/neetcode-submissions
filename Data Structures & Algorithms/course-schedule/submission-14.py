class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build adj List
        # fill inDegree arraay
        # push all items with inDegree == 0 to the queue 
        # pop from the queue mark as visited and push all that has inDegree 0

        adjList = {}
        total = 0
        for n in range(numCourses):
            adjList[n] = []
        
        inDegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            inDegree[course]+= 1
        
        q = deque()

        for n in range(numCourses):
            if inDegree[n] == 0:
                q.append(n)
        

        while(q):
            course = q.popleft()
            total += 1
            for adj in adjList[course]:
               inDegree[adj] -= 1
               
               if inDegree[adj] == 0:
                q.append(adj)
            


        return total == numCourses