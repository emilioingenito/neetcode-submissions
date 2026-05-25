# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([(root, 0)])
        level, current_layer, all_layers = 0, [], []
        
        while queue:
            node, current_level = queue.popleft()

            if current_level != level:
                all_layers.append(current_layer)
                current_layer, level = [], current_level

            current_layer.append(node.val)
            if node.left:
                queue.append((node.left, current_level+1))
            if node.right:
                queue.append((node.right, current_level+1))
        
        all_layers.append(current_layer)
        return all_layers