class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, time in times:
            adj[source].append((target, time))
        visited = set()

        heap = [(0,k)]
        t = 0

        while heap:
            w, node =  heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = w
            
            for target, time in adj[node]:
                if target not in visited:
                    heapq.heappush(heap, (time + w, target))
        
        return t if len(visited) == n else -1 