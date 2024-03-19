# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inoder(root):
            if root is None:
                return []
            return inoder(root.left) + [root.val] + inoder(root.right)
        nums = inoder(root)
        root = TreeNode(nums[0])
        head = root
        for num in nums[1:]:
            root.right = TreeNode(num)
            root = root.right
        return head
