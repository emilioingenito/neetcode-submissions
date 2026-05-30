from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = self.build(n, edges)

        queue, visited = deque([(0, set())]), set()
        while queue:
            node, parents = queue.popleft()

            if node in visited:
                return False
            
            visited.add(node)
            updated_parents = parents.copy()
            updated_parents.add(node)
            for neighbor in graph[node]:
                if neighbor not in parents:
                    queue.append((neighbor, updated_parents))
        
        return len(visited) == n
    

    def build(self, n: int, edges: List[List[int]]) -> dict:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        return graph