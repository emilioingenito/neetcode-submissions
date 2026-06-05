class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, total = [float('-inf')] * len(height), [float('-inf')] * len(height), 0

        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        
        for i, h in enumerate(height):
            total += max(min(left[i], right[i]) - h, 0)
            
        return total