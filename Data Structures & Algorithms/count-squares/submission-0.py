from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        counter, (x, y) = 0, point
        for b in self.points.keys():
            x1, y1 = b
            if (x, y) != b and abs(x - x1) == abs(y - y1):
                c, d = (x1, y), (x, y1)
                if c not in self.points or d not in self.points:
                    continue
                squares = self.points[b] * self.points[c] * self.points[d]
                if (x, y) in self.points:
                    squares *= self.points[(x, y)]
                counter += squares 
        return counter