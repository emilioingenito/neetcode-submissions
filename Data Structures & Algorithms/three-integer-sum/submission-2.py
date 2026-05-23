class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums.sort()
        ans = set()
        for idx, n in enumerate(nums):
            target = -n
            left, right = idx+1, len(nums)-1

            while left < right:
                partial_sum = nums[left] + nums[right]
                if partial_sum == target:
                    ans.add(tuple([n, nums[left], nums[right]]))
                    left, right = left+1, right-1
                elif partial_sum > target:
                    right -= 1
                else:
                    left +=1
        
        return list(ans)
        '''
        nums.sort()
        ans, idx = [], 0
        while idx < len(nums):
            while 0 < idx < len(nums)-1 and nums[idx] == nums[idx-1]:
                idx += 1

            target = - nums[idx]
            left, right = idx+1, len(nums)-1

            while left < right:
                partial_sum = nums[left] + nums[right]
                if partial_sum == target:
                    ans.append([nums[idx], nums[left], nums[right]])
                    left, right = self.move(nums, left+1, True), self.move(nums, right-1, False)
                elif partial_sum > target:
                    right = self.move(nums, right-1, False)
                else:
                    left = self.move(nums, left+1, True)
            
            idx += 1
        
        return list(ans)
    
    
    def move(self, nums: List[int], idx: int, right: bool) -> int:
        if right: 
            while idx < len(nums) and nums[idx] == nums[idx-1]:
                idx += 1
            return idx
        else:
            while 0 <= idx and nums[idx] == nums[idx+1]:
                idx -= 1
            return idx



