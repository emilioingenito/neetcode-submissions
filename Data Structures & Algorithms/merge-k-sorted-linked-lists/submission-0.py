# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [(node.val, node) for node in lists]
        heapq.heapify(lists)
        current = head = ListNode()
        while lists:
            _, node = heapq.heappop(lists)
            current.next = node
            current = current.next
            if current.next:
                heapq.heappush(lists, (current.next.val, current.next))

        return head.next