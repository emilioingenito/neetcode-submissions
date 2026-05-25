"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head:'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None

        nodes_position, current, counter = {}, head, 0
        while current:
            nodes_position[current] = counter
            counter += 1
            current = current.next

        copied_nodes = []
        for n in range(counter):
            copied_nodes.append(Node(0))
        copied_nodes.append(None)

        current, counter = head, 0
        while current:
            copied = copied_nodes[counter]
            copied.val = current.val
            copied.next = copied_nodes[counter+1]
            
            if current.random != None:
                copied.random = copied_nodes[nodes_position[current.random]]
            current = current.next
            counter += 1

        return copied_nodes[0]