from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[b].append(a)
            in_degree[a] += 1
        
        queue = deque([course for course in range(numCourses) if in_degree[course]==0])
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return all([dependencies == 0 for dependencies in in_degree.values()])
            
