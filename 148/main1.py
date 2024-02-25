# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.sort()
        res = ListNode()
        dummy = res
        for num in nums:
            node = ListNode(num)
            res.next = node
            res = res.next
        return dummy.next
