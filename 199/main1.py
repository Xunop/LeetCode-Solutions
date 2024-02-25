# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        queue = []
        queue.append(root)

        while len(queue) > 0:
            size = len(queue)
            item = []
            while size > 0:
                curNode = queue.pop(0)
                item.append(curNode.val)
                if curNode.left is not None:
                    queue.append(curNode.left)
                if curNode.right is not None:
                    queue.append(curNode.right)
                size -= 1
            res.append(item.pop())
        return res
