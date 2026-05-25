class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums: return -1
        slow = fast = 0

        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        
        return slow