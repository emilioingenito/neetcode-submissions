from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree, graph = self.build(edges)
        starting_nodes = [node for node in range(1, len(edges)+1) if indegree[node] == 1]
        queue = deque((node, -1) for node in starting_nodes)
        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append((neighbor, node))

        # Once processed the nodes, we're left with the cycle
        cycle = set([node for node in range(1, len(edges)+1) if indegree[node] > 1])
        return next(edge for edge in reversed(edges) if edge[0] in cycle and edge[1] in cycle)


    def build(self, edges: List[List[int]]) -> (dict, dict):
        indegree, graph = defaultdict(int), defaultdict(list)

        for start, end in edges:
            indegree[start] += 1
            indegree[end] += 1
            graph[start].append(end)
            graph[end].append(start)
        
        return indegree, graph