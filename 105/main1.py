# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = preorder[0]
        root_index = inorder.index(root)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        left = self.buildTree(left_preorder, left_inorder) if left_inorder else None
        right = self.buildTree(right_preorder, right_inorder) if right_inorder else None
        return TreeNode(root, left, right)
