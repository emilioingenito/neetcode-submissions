from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans, in_degree, adj_list = [], defaultdict(int), defaultdict(list)
        for a, b in prerequisites:
            in_degree[a] += 1
            adj_list[b].append(a)

        no_prerequisites = [course for course in range(numCourses) if in_degree[course] == 0]
        queue = deque(no_prerequisites)

        while queue:
            course = queue.popleft()
            ans.append(course)
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return ans if len(ans) == numCourses else []