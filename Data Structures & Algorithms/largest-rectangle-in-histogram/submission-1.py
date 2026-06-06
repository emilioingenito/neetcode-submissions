class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest, stack = 0, []
        # stack -> height, index
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= h:
                h_prev, i_prev = stack.pop()
                largest = max(largest, (i - i_prev) * h_prev)
                start = i_prev
            stack.append((h, start))

        for h, i in stack:
            largest = max(largest, (len(heights)-i) * h)

        return largest