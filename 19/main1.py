# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l1 = head
        while n:
            l1 = l1.next
            n -= 1
        if not l1:
            return head.next
        l2 = head
        while l1.next:
            l1 = l1.next
            l2 = l2.next
        l2.next = l2.next.next
        return head
