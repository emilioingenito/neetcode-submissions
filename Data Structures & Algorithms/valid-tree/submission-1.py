from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = self.build(n, edges)

        queue, visited = deque([(0, -1)]), set()
        while queue:
            node, parent = queue.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    queue.append((neighbor, node))
        
        return len(visited) == n
    

    def build(self, n: int, edges: List[List[int]]) -> dict:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        return graph