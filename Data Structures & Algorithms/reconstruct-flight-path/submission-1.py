class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in tickets:
            heapq.heappush(graph[start], end)

        path = []
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            path.append(node)

        dfs('JFK')
        return path[::-1]