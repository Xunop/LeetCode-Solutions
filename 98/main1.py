# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l = self.isValidBST(root.left)
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        r = self.isValidBST(root.right)
        return l and r
