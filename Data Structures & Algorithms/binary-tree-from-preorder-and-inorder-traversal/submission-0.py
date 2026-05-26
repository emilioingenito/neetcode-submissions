# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Inorder tells me about the split: SX - ME - DX
        # Preorder tells me about the next: ME - SX  - DX

        def build(a, b, x, y):
            if a > b and x > y:
                return None
            
            value = preorder[a]
            node = TreeNode(value)
            tmp = None

            for i in range(x, y+1):
                if inorder[i] == value:
                    tmp = i

            node.left = build(a+1, a+(tmp-x), x, tmp-1)
            node.right = build(a+(tmp-x)+1, b, tmp+1, y)

            return node
        
        return build(0, len(preorder)-1, 0, len(inorder)-1)
        