class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adjList = new ArrayList<>();
        List<Integer> schedule = new ArrayList<>();

        for (int i = 0; i < numCourses; i++){
            adjList.add(new ArrayList<>());
        }

        int[] inDegree = new int[numCourses];
        for (int[] dependency : prerequisites){
            int course = dependency[0];
            int prereq = dependency[1];

            adjList.get(prereq).add(course);
            inDegree[course]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < numCourses; i++){
            if (inDegree[i] == 0) queue.offer(i);
        }

        while (!queue.isEmpty()){
            int course = queue.poll();
            schedule.add(course);

            for (int next : adjList.get(course)){
                if (--inDegree[next] == 0) queue.offer(next);
            }
        }

        int[] res = schedule.stream().mapToInt(Integer::intValue).toArray();
        return res.length == numCourses? res  : new int[0];
    }
}
