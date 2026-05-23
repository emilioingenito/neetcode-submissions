from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for char in s:
                counter[ord(char) - ord('a')] += 1
            d[tuple(counter)].append(s)
        return list(d.values())