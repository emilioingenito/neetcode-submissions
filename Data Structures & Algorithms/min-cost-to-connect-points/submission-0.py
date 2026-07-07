class UnionFind:
    def __init__(self, points):
        self.parent, self.rank = defaultdict(int), defaultdict(int)
        for p in points:
            self.parent[tuple(p)] = tuple(p)
            self.rank[tuple(p)] = 0

    
    def find(self, a):
        if self.parent[a] == self.parent[self.parent[a]]:
            return self.parent[a]
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    

    def union(self, a, b, dst):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return 0
        if self.rank[b] > self.rank[a]:
            self.parent[a] = b
        elif self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.rank[a] += 1
            self.parent[b] = a
        return dst


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        queue = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i]
                x, y = points[j]
                dst = abs(a-x) + abs(b-y)
                queue.append((dst, points[i], points[j]))
        queue.sort()
        cost, uf = 0, UnionFind(points)
        for dst, a, b in queue:
            cost += uf.union(tuple(a), tuple(b), dst)
        return cost