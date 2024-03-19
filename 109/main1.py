# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def link_to_arr(head, arr):
            while head:
                val = head.val
                arr.append(val)
                head = head.next

        def arr_to_BST(nums):
            if not nums:
                return None
            mid = len(arr) // 2
            root = TreeNode(nums[mid])
            root.left = arr_to_BST(nums[:mid])
            root.right = arr_to_BST(nums[mid+1:])
            return root

        nums = link_to_arr(head, [])
        return arr_to_BST(nums)
