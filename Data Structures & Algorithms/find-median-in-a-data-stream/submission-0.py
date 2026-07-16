import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = [] # left side
        self.minheap = [] # right side

    def addNum(self, num: int) -> None:
        # Insert
        if not self.minheap:
            self.minheap = [num]
        elif not self.maxheap:
            self.maxheap = [num]
            if self.maxheap[0] > self.minheap[0]:
                self.maxheap, self.minheap = self.minheap, self.maxheap
        elif num <= self.maxheap[0]:
            heapq.heappush_max(self.maxheap, num)
        else:
            heapq.heappush(self.minheap, num)
        
        # Rebalance the 2 heaps
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush_max(self.maxheap, heapq.heappop(self.minheap))
        elif len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, heapq.heappop_max(self.maxheap))
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        return (self.maxheap[0] + self.minheap[0]) / 2