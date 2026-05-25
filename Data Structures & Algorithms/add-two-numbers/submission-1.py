# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder, head = 0, ListNode()
        prev = head
        
        while l1 or l2 or remainder:
            l1_value = 0 if not l1 else l1.val
            l2_value = 0 if not l2 else l2.val
            
            total = l1_value + l2_value + remainder
            value = total % 10
            remainder = total // 10
            curr = ListNode(value)
            prev.next = curr
            prev = curr

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next



