# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.scanTree(root))

    # [maxDepth, maxPath]
    def scanTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return (0, 0)
        left = self.scanTree(root.left)
        right = self.scanTree(root.right)

        path = 2 if root.left and root.right else 1 if root.left else 1 if root.right else 0
        depth = 1 if root.left or root.right else 0
        return (
            depth + max(left[0], right[0]),
            max(left[1], right[1], path + left[0] + right[0])
        )
    '''

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def height(node):
            if not node:
                return 0
            
            left, right = height(node.left), height(node.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        height(root)
        return self.ans