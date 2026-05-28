class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def backtrack(current, seen):
            nonlocal permutations
            if len(current) == len(nums):
                permutations.append(current[:])
                return 
            
            for n in nums:
                if n in seen:
                    continue
                seen.add(n)
                current.append(n)
                backtrack(current, seen)
                current.pop()
                seen.remove(n)


        backtrack([], set())
        return permutations