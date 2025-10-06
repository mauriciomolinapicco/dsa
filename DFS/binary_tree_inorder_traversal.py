# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        
        def dfs_inorder(obj):
            if obj == None: return
            dfs_inorder(obj.left)
            result.append(obj.val)
            dfs_inorder(obj.right)
        
        dfs_inorder(root)

        return result