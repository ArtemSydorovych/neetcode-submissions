class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for source, target, time in times:
            adj[source].append((target, time))

        heap = [(0,k)]
        visited = set()
        t = 0
        while heap:
            time, source = heapq.heappop(heap)

            if source in visited:
                continue    
            visited.add(source)
            t = time


            for target, tm in adj[source]:
                
                if target in visited:
                    continue

                heapq.heappush(heap, (time + tm, target))


        return t if len(visited) == n else -1