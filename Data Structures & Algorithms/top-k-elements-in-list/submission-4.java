class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();

        for (int n : nums) counts.merge(n, 1, Integer::sum);
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> counts.get(a) - counts.get(b));

        for (int num : counts.keySet()){
            pq.offer(num);
            if(pq.size() > k) pq.poll();
        }

        return pq.stream().mapToInt(Integer::intValue).toArray();
    }
}
