class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        List<Integer> completed = new ArrayList<>();
        for (int i = 0; i < numCourses; i++){
            adj.add(new ArrayList<>());
        }

        int[] inDegree = new int[numCourses];

        for (int[] p : prerequisites){
            int course = p[0], prereq = p[1];
            adj.get(prereq).add(course);
            inDegree[course]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < numCourses; i++){
            if(inDegree[i] == 0) queue.offer(i);
        }

        while(!queue.isEmpty()){
            int course = queue.poll();
            completed.add(course);

            for (int next : adj.get(course)){
                if (--inDegree[next] == 0){
                    queue.offer(next);
                }
            } 
        }

        return completed.size() == numCourses ? completed.stream().mapToInt(Integer::intValue).toArray() : new int[0];
    }
}
