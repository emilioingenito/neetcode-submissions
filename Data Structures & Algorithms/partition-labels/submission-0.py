from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        furthest = defaultdict(int)
        for i, c in enumerate(s):
            furthest[c] = max(furthest[c], i)
        l = curr_max = 0
        labels = []
        for i, c in enumerate(s):
            curr_max = max(curr_max, furthest[c])
            if curr_max <= i:
                labels.append(i-l+1)
                l = i+1
                current_max = 0
        return labels