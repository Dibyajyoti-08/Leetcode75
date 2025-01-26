# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        from collections import deque
        q1, q2 = deque(), deque()
        def findleaf(root, result):
            if root.left is None and root.right is None:
                result.append(root.val)
                return
            if root.left:
                findleaf(root.left, result)
            if root.right:
                findleaf(root.right, result)
            return
        findleaf(root1, q1)
        findleaf(root2, q2)
        return q1==q2
            
        