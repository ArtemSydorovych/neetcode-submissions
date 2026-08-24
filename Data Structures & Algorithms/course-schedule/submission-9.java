class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adjList = new ArrayList<>();
        int visited = 0;

        for (int i = 0; i < numCourses; i++){
            adjList.add(new ArrayList<>());
        }

        int[] inDegree = new int[numCourses];
        for (int[] pair : prerequisites){
            int course = pair[0], prereq = pair[1];
            inDegree[course]++;
            adjList.get(prereq).add(course);
        }

        Deque<Integer> coursesQueue = new ArrayDeque<>();

        for(int i = 0; i < numCourses; i++){
            if(inDegree[i] == 0){
                coursesQueue.offer(i);
            }
        }
        
        while (!coursesQueue.isEmpty()){
            int course = coursesQueue.poll();
            visited++;

            for (int next : adjList.get(course)){
                if(--inDegree[next] == 0){
                    coursesQueue.offer(next);
                }
            }
        }


        return visited == numCourses;
    }
}
