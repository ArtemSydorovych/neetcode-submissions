class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
            List<List<Integer>> adj = new ArrayList<>();

            for (int i = 0; i < numCourses; i++){
                adj.add(new ArrayList<>());
            }

            int[] inDegree = new int[numCourses];

            for (int[] p : prerequisites) {
                int course = p[0], prereq = p[1];
                adj.get(prereq).add(course);
                inDegree[course]++;
            }

            Deque<Integer> queue = new ArrayDeque<>();
            for (int i = 0; i < numCourses; i++){
                if (inDegree[i] == 0) queue.offer(i);
            }

            int completed = 0;

            while (!queue.isEmpty()){
                int course = queue.poll();
                completed++;

                for (int next : adj.get(course)){
                    if (--inDegree[next] == 0){
                        queue.offer(next);
                    }
                }
            }

            return completed == numCourses;
    }
}
