class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for source, target, time in times:
            adj[source].append((target, time))
        
        heap = [(0, k)]
        visited = set()
        res = 0

        while heap:
            time, source = heapq.heappop(heap)

            if source in visited:
                continue
            res = time
            visited.add(source)

            for target, t in adj[source]:
                if target not in visited:
                    heapq.heappush(heap, (t + time, target))


        return res if len(visited) == n else - 1