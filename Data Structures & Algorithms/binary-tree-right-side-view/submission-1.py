# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue, layers = deque([root]), []

        while queue:
            visible_element = None
            for _ in range(len(queue)):
                node = queue.popleft()
                visible_element = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            layers.append(visible_element.val)

        return layers