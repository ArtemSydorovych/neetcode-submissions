from _heapq import heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for val, freq in counts.items():
            heapq.heappush(heap, (freq, val))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for freq, val in heap]