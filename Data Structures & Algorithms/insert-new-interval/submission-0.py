class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans, i = [], 0

        while i <= len(intervals):
            if i == len(intervals):
                ans.append(newInterval)
                break

            start, end = newInterval
            interval = intervals[i]
            prev_start, prev_end = interval
		
            if prev_end < start:
                ans.append(interval)
                i += 1
            elif end < prev_start:
                ans.append(newInterval)
                ans.extend(intervals[i:]) 
                break
            else:
                newInterval = [min(prev_start, start), max(prev_end, end)]
                i += 1

        return ans