class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, time in times:
            adj[source].append((target, time))

        heap = [(0,k)]
        dist = {}

        while heap:
            timeToNode, node = heapq.heappop(heap)
            if node in dist:
                continue
            
            dist[node] = timeToNode

            for (target,time) in adj[node]:
                if target not in dist:
                    heapq.heappush(heap, (timeToNode +  time,target))
        
        return max(dist.values()) if len(dist) == n else -1