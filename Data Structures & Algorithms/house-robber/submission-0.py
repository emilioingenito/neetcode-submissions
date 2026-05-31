class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        loot = [0] * (len(nums)-2) + nums[-2:][:]
        for i in range(len(nums)-3, -1, -1):
            loot[i] = max(loot[i+1], nums[i] + loot[i+2])
        
        return loot[0]