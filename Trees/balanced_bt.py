"""
 height-balanced binary tree is a binary tree in which the depth of the 
 two subtrees of every node never differs by more than one
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        def depth(root):
            if root == None: return 0
            return max(depth(root.left), depth(root.right)) + 1
        ld = depth(root.left)
        rd = depth(root.right)

        if abs(ld-rd) > 1: return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)