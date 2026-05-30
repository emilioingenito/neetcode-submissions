from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.build(times)
        queue, visited, max_delay = [(0, k)], set(), 0
        
        while queue:
            delay, element = heapq.heappop(queue)
            if element in visited:
                continue
            visited.add(element)
            max_delay = max(max_delay, delay)
            for (neighbor, weight) in graph[element]:
                if neighbor not in visited:
                    heapq.heappush(queue, (delay+weight, neighbor))
        
        return max_delay if len(visited) == n else -1


    def build(self, times: List[List[int]]) -> dict:
        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end, weight))
        return graph