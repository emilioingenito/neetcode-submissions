# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, nodeA: Optional[TreeNode], nodeB: Optional[TreeNode]) -> bool:
        if not nodeA and not nodeB:
            return True
        
        if not nodeA or not nodeB:
            return False
        
        return nodeA.val == nodeB.val and self.isSameTree(nodeA.left, nodeB.left) and self.isSameTree(nodeA.right, nodeB.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        
        if not root or not subRoot:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        