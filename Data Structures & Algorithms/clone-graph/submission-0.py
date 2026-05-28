"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        newNodes, queue = {node: Node(node.val)}, deque([node])
        
        while queue:
            current = queue.popleft()
            for n in current.neighbors:
                if n not in newNodes:
                    newNodes[n] = Node(n.val)
                    queue.append(n)
        
        for old, current in newNodes.items():
            for n in old.neighbors:
                current.neighbors.append(newNodes[n])
        
        return newNodes[node]



        