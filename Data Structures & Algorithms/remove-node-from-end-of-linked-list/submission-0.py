# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def count(self, head: Optional[ListNode]) -> int:
        count = 0 
        while head:
            count += 1
            head = head.next
        return count


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target = self.count(head) - n
        if target == 0:
            return head.next

        prev, curr = None, head
        while target != 0:
            prev = curr
            curr = curr.next
            target -= 1

        prev.next = curr.next 
        return head
