# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#|'
        return str(root.val) + '|' + self.serialize(root.left) + self.serialize(root.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        def dfs(index):
            if index >= len(data) or data[index] == '#':
                return index+1, None
            idx = self.delimit(index, data)
            right_index, left_node = dfs(idx+1)
            next_index, right_node = dfs(right_index+1)
            current_node = TreeNode(int(data[index:idx]), left_node, right_node)
            return next_index, current_node

        return dfs(0)[1]
    

    def delimit(self, index, data) -> int:
        while index < len(data) and data[index] != '|':
            index += 1
        return index