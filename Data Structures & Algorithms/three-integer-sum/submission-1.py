class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
                

