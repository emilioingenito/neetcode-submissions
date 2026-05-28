class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtracking(current, index, target):
            if target == 0:
                combinations.append(current[:])
                return
            
            if index == len(candidates) or target < 0:
                return

            backtracking(current + [candidates[index]], index+1, target-candidates[index])
            index = index+1
            while index < len(candidates) and candidates[index]==candidates[index-1]:
                index += 1
            backtracking(current, index, target)


        backtracking([], 0, target)
        return combinations
        