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
    max_dis = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def max_depth(root):
            if root == None: return 0
            return max(max_depth(root.left), max_depth(root.right)) + 1
        
        def dfs(root):
            if root == None: return
            current_dis = max_depth(root.left) + max_depth(root.right)
            if current_dis > self.max_dis: self.max_dis = current_dis
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.max_dis
