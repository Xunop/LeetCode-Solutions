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
        def inorder(root: Optional[TreeNode]) -> List[int]:
                if root is None:
                    return []
                return inorder(root.left) + [root] + inorder(root.right)
        
        def find_swapped_node(nodes):
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
            print('x:' + x)
            print('y:' + x)
            if root:
                if root.val == x:
                    root.val = y
                elif root.val == y:
                    root.val = x
                recover_tree(root.left, x, y)
                recover_tree(root.right, x, y)

        nodes = inorder(root)
        # x > y
        x, y = find_swapped_node(nodes)
        print(x.val, y.val)
        recover_tree(root, x.val, y.val)
