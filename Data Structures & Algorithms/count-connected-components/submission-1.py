from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components, visited, graph = 0, set(), self.build(n, edges)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                self.bfs(node, visited, graph)
                components +=1
        
        return components
    

    def bfs(self, n: int, visited: set, graph: dict) -> None:
        queue = deque([n])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # Nothing to return, modifies the visited set in-place
        return


    def build(self, n: int, edges: List[List[int]]) -> dict:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        return graph