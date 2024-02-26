# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)

    # 1. p,q都能找到返回最近公共祖先 2. p,q 找到一个，返回p/q 3. 都没找到返回 null
    def helper(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        if left and right:
            return root
        return left if left else right

