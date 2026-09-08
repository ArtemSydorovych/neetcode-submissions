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

        for course, prereq in prerequisites:
            adjList[prereq].append(course)  

        visiting = set()
        def dfs(course):
            if course in visiting:
                return False

            if adjList[course] == []:
                return True
            
            visiting.add(course)

            for pre in adjList[course]:
                if not(dfs(pre)):
                    return False
            
            visiting.remove(course)
            adjList[course] = []
            return True


        for c in range(numCourses):
            if not(dfs(c)):
                return False
        

        return True







