class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = []
        intervals.sort()

        for interval in intervals:
            start, end = interval
            if not ans or ans[-1][1] <= start:
                ans.append(interval)
            
            else:
                prev = ans.pop()
                keep = interval if end < prev[1] else prev
                ans.append(keep)

        return len(intervals) - len(ans)