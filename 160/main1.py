# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashMap = {}
        while headA:
            hashMap[headA] = True
            headA = headA.next
        while headB:
            if headB in hashMap:
                return headB
            headB = headB.next
        return None
