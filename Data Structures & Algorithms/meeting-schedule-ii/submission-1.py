"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        free_rooms, min_rooms = [], 0

        for interval in intervals:
            if not free_rooms or free_rooms[0] > interval.start:
                min_rooms += 1
                heapq.heappush(free_rooms, interval.end)
            else:
                heapq.heappushpop(free_rooms, interval.end)

        return min_rooms