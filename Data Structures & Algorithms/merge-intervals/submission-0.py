class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for interval in intervals:
            start, end = interval
            if not ans or ans[-1][1] < start:
                ans.append(interval)
            else:
                prev_start, prev_end = ans.pop()
                ans.append([min(start, prev_start), max(end, prev_end)])
        return ans