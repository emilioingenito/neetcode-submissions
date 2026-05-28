class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []

        def backtrack(current, index):
            if index == len(s):
                partitions.append(current[:])
                return
            
            for i in range(index, len(s)):
                if s[index:i+1] == s[index:i+1][::-1]:
                    current.append(s[index:i+1])
                    backtrack(current, i+1)
                    current.pop()


        backtrack([], 0)
        return partitions