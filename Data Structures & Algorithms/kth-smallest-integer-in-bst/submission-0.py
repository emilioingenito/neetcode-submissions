# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = -1
        self.k = k

        def find_smallest(root) -> None:
            if not root or self.k <= 0:
                return
            find_smallest(root.left)
            self.k -= 1
            if self.k == 0:
                self.smallest = root.val
            else:
                find_smallest(root.right)
        
        find_smallest(root)
        return self.smallest


        