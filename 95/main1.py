# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def dfs(l, r):
            if l > r:
                return [None]
            ans = []
            for i in range(l, r + 1):
                for x in dfs(l, i - 1):
                    for y in dfs(i + 1, r):
                        root = TreeNode(i)
                        root.left, root.right = x, y
                        ans.append(root)
            return ans
        return dfs(1, n)
