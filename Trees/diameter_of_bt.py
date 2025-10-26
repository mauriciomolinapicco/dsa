""" NOTE
Actually diameter means max length betw 2 nodes
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dis = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # actualizar diámetro global
            self.max_dis = max(self.max_dis, left + right)
            # devolver la altura de este nodo
            return 1 + max(left, right)

        depth(root)
        return self.max_dis
