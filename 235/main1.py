# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inoder(root, p, q):
            if not root or root == p or root == q:
                return root
            left = inoder(root.left, p, q)
            right = inoder(root.right, p, q)
            return left if left else right
        return inoder(root, p, q)
