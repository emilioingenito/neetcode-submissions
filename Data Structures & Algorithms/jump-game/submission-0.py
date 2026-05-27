class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: 
            return True

        closest = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= closest:
                closest = i
        
        return closest == 0