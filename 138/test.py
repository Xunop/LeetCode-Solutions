class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

node3 = Node(3, None, None)
node2 = Node(2, node3, None)
node = Node(1, node2, node3)

dummy = node
while dummy:
    print(dummy.val)
    dummy.val = 9
    print(dummy.val)
    dummy = dummy.next 

while node:
    print(node.val)
    node = node.next
