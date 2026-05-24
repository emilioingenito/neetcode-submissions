# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def count(self, head: Optional[ListNode]) -> None:
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    

    def reverse(self, head: Optional[ListNode], count: int) -> None:
        half, idx, prev = count//2, 0, head

        while idx <= half:
            prev = head
            head = head.next
            idx += 1
        
        prev.next = None
        prev = None

        while head:
            succ = head.next
            head.next = prev
            prev = head
            head = succ
        
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        count = self.count(head)
        reverse = self.reverse(head, count)

        while head and reverse:
            succ_head = head.next
            succ_reverse = reverse.next
            head.next = reverse
            reverse.next = succ_head
            head = succ_head
            reverse = succ_reverse