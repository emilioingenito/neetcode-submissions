# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def scanTree(root: TreeNode, currentMax: int) -> int:
            if not root:
                return 0

            goodNode = 1 if root.val >= currentMax else 0
            newMax = max(currentMax, root.val)
            return goodNode + scanTree(root.left, newMax) + scanTree(root.right, newMax)

        return scanTree(root, root.val if root else -1)