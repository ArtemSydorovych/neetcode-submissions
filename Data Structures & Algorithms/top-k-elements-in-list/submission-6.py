class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for val, frq in freq.items():
            heapq.heappush(heap, (frq, val));
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for freq, val in heap]