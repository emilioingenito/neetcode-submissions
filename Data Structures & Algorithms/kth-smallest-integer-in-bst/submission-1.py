# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result, count = -1, k

        def find_smallest(root) -> None:
            nonlocal result, count
            if not root or count <= 0:
                return
            find_smallest(root.left)
            count -= 1
            if count == 0:
                result = root.val
            else:
                find_smallest(root.right)
        
        find_smallest(root)
        return result


        