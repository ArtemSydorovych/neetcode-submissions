class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adjList = new ArrayList<>();
        int visited = 0;
        for (int i = 0; i < numCourses; i++){
            adjList.add(new ArrayList<>());
        }

        int[] inDegree = new int[numCourses];
        for(int[] pair : prerequisites){
            int course = pair[0], prerequisite = pair[1];
            inDegree[course]++;
            adjList.get(prerequisite).add(course);
        }


        Deque<Integer> queue = new ArrayDeque<>();
        
        for (int i = 0; i < numCourses; i++){
            if (inDegree[i] == 0) queue.offer(i);
        }
        
        while(!queue.isEmpty()){
            int course = queue.poll();
            visited++;

            for(int next : adjList.get(course)){
                if (--inDegree[next] == 0) queue.offer(next);
            }
        }


        return visited == numCourses;
    }
}
