"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # create a new node for each node and put it next to the original node
        cur = head
        while cur:
            new_node = Node(cur.val, cur.next)
            cur.next = new_node
            cur = new_node.next
        # assign random pointer for the new node
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # split the new list from the original list
        cur = head
        new_head = head.next
        new_cur = new_head
        while cur:
            cur.next = new_cur.next
            cur = cur.next
            if cur:
                new_cur.next = cur.next
                new_cur = new_cur.next
        return new_head
