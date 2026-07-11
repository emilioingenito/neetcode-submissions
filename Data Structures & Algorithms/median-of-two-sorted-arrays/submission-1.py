class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, large = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        N, M = len(small), len(large)
        T, HALF = N+M, (N+M+1)//2
        l, r = 0, len(small)

        while l <= r:
            i = l + (r-l)//2
            
            j = HALF - i
            Aleft = small[i-1] if i > 0 else float('-inf')
            Aright = small[i] if i < N else float('inf')
            Bleft = large[j-1] if j > 0 else float('-inf')
            Bright = large[j] if j < M else float('inf')

            if Bleft <= Aright and Aleft <= Bright:
                return max(Aleft, Bleft) if T % 2 != 0 else (max(Aleft,Bleft) + min(Aright, Bright))/2
            if Bleft > Aright:
                l = i + 1
            else:
                r = i - 1
        
        raise Exception("Malformed input")