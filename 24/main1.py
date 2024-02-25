# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first, slow = head.next, head
        while first and slow:
            first.val, slow.val = slow.val, first.val
            if not first.next or not first.next.next:
                break
            first = first.next.next
            slow = slow.next.next
        return head
