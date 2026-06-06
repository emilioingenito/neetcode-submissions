from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, freq, goal, done = 0, defaultdict(int), Counter(t), set()
        min_len, indeces = float('inf'), (-1,-1)

        for r, c in enumerate(s):
            if c in goal:
                freq[c] += 1
                if freq[c] >= goal[c]:
                    done.add(c)

            while len(done) == len(goal):
                if r-l < min_len:
                    indeces = (l, r)
                    min_len = r-l
                if s[l] in freq:
                    freq[s[l]] -= 1
                    if freq[s[l]] < goal[s[l]]:
                        done.remove(s[l])
                l += 1
        
        return s[indeces[0]:indeces[1]+1] if indeces != (-1, -1) else ""