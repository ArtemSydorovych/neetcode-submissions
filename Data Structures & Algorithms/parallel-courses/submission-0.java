class Solution {
    public int minimumSemesters(int n, int[][] relations) {
        List<List<Integer>> adj = new ArrayList<>();

        for (int i = 0; i <= n; i++){
            adj.add(new ArrayList<>());
        }

        int[] inDegree = new int[n+1];

        for (int[] p : relations){
            int course = p[1], prereq = p[0];
            adj.get(prereq).add(course);
            inDegree[course]++;
        }

        List<Integer> queue = new ArrayList<>();

        for(int i = 1; i <= n; i++){
            if (inDegree[i] == 0) queue.add(i);
        }

        int semesters = 0;
        int coursesCompleted = 0;
        while(!queue.isEmpty()){
            semesters++;
            List<Integer> nextQueue = new ArrayList<>();
            
            for (int node : queue){
                coursesCompleted++;
                for (int next : adj.get(node)){
                    if(--inDegree[next] == 0){
                        nextQueue.add(next);
                    }
                }
            }

            queue = nextQueue;
        }

        return coursesCompleted == n? semesters : -1;
    }
}
