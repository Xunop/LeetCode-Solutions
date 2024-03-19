# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root
                yield from inorder(root.right)
        
        def find_swapped_nodes(nodes):
            x = y = None
            for i in range(len(nodes) - 1):
                if nodes[i].val > nodes[i + 1].val:
                    y = nodes[i + 1]
                    if x is None:
                        x = nodes[i]
                    else:
                        break
            return x, y
        
        def recover_tree(root, x, y):
            if root:
                if root.val == x.val:
                    root.val = y.val
                elif root.val == y.val:
                    root.val = x.val
                recover_tree(root.left, x, y)
                recover_tree(root.right, x, y)
        
        nodes = list(inorder(root))
        print(nodes)
        x, y = find_swapped_nodes(nodes)
        recover_tree(root, x, y)
        return root
