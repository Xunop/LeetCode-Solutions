# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {}
        cur = head
        while cur:
            if cur in hashMap:
                return cur
            hashMap[cur] = True
            cur = cur.next
        return None
