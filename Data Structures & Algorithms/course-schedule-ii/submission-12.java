class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adjList = new ArrayList<>();
        int visited = 0;
        int[] visitedArr = new int[numCourses];

        for (int i = 0; i < numCourses; i++){
            adjList.add(new ArrayList<>());
        }
        
        int[] inDegree = new int[numCourses];
        
        for (int[] pair : prerequisites){
            int course = pair[0], prerequisite = pair[1];
            adjList.get(prerequisite).add(course);
            inDegree[course]++;
        }
    
        Deque<Integer> queue = new ArrayDeque<Integer>();

        for (int i = 0; i < numCourses; i++){
            if(inDegree[i] == 0) queue.offer(i);
        }

        while(!queue.isEmpty()){
            int course = queue.poll();
            visitedArr[visited++] = course;
            for(int next : adjList.get(course)){
                if (--inDegree[next] == 0) queue.offer(next);
            }
        }

        return visited == numCourses? visitedArr : new int[0];
    }
}
