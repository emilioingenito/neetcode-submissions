# Definition for double-linked list.
class Node:
    def __init__(self, val=0, key=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.put(key, self.nodes[key].val)
        return self.nodes[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])
        elif self.current_size == self.capacity:
            self.remove(self.head.next)

        node = Node(value, key, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.current_size += 1
        self.nodes[key] = node


    def remove(self, node: Optional('Node')):
        del self.nodes[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.current_size -= 1