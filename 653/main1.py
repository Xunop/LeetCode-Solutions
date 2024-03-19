# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.set = set()
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.set:
            return True
        self.set.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
