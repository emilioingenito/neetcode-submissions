class Solution:
    def findMin(self, nums: List[int]) -> int:
        self.min, left, right = float('inf'), 0, len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            self.min = min(self.min, nums[mid])

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid +1
        
        return self.min

            