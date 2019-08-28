# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = []
        self.dfs(root)
        return sum(self.res)
    def dfs(self,curr):
        if not curr:
            return
        if curr.left:
            if not curr.left.left and not curr.left.right:
                self.res.append(curr.left.val)
        self.dfs(curr.left)
        self.dfs(curr.right)
        