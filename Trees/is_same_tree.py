class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return True if (q is None and p is None) else False 
        return p.val == q.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)