# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -sys.maxsize - 1
        def dfs(root):
            if not root:
                return -sys.maxsize - 1
            left = dfs(root.left)
            right = dfs(root.right)
            # root + left + right, left, right, root cannot be added up
            self.maxSum = max(root.val + left + right, left, right, self.maxSum)
            # root + left, root + right, root can be added up
            return max(root.val + left, root.val + right, root.val)

        newMax = dfs(root)
        return max(self.maxSum, newMax)
