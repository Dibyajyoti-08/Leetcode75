# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.gn = 0
        def gnbt(root, mxm):
            if root.val >= mxm: self.gn += 1
            if root.left: gnbt(root.left, max(mxm, root.val))
            if root.right: gnbt(root.right, max(mxm, root.val))
        gnbt(root, root.val)
        return self.gn
        