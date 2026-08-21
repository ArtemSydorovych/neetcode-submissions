class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adjList = new ArrayList();
        int[] result = new int[numCourses];
        int current = 0;
        for (int i = 0; i < numCourses; i++){
            adjList.add(new ArrayList<>());
        }

        int[] inDegree = new int[numCourses];

        for (int[] pair : prerequisites){
            int course = pair[0];
            int prerq = pair[1];

            adjList.get(prerq).add(course);
            inDegree[course]++;    
        }        


        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++){
            if (inDegree[i] == 0) queue.offer(i);
        }

        while (!queue.isEmpty()){
            int course = queue.poll();
            result[current++] = course;

            for (int next : adjList.get(course)){
                if (--inDegree[next] == 0) queue.offer(next);
            }
        }


        return current == numCourses ? result : new int[0];
    }
}
