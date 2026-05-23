import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        idx = bisect.bisect_left(nums, target)
        return idx if idx < len(nums) and nums[idx] == target else -1
        '''

        left, right = 0, len(nums)-1
        while left <= right: 
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1