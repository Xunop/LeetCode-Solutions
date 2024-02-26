# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + self.dfs(root, targetSum)

    def dfs(self, root, targetSum):
        if root is None:
            return 0
        targetSum -= root.val
        return (1 if targetSum == 0 else 0) + self.dfs(root.left, targetSum) + self.dfs(root.right, targetSum)
