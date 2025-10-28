# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def is_same_tree(self, root,subRoot): #dfs
        if root is None and subRoot is None: return True
        if not root and subRoot: return False
        if root and not subRoot: return False
        if root.val != subRoot.val: return False
        return self.is_same_tree(root.left, subRoot.left) and self.is_same_tree(root.right, subRoot.right)

    # bfs to iterate through all nodes of tree. DFS on BFS
    def isSubtree(self, root, subRoot):
        cola = deque()
        cola.append(root)
        while len(cola) > 0:
            r = cola.popleft()
            result = self.is_same_tree(r, subRoot)
            if result: return True
            if r.left is not None: cola.append(r.left)
            if r.right is not None: cola.append(r.right)
        return False
