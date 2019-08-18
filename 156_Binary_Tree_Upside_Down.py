# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            return self.dfs(root)
    
    def dfs(self,curr):
        if not curr.left:
            return curr
        leftans = self.dfs(curr.left)
        curr.left.right = curr
        curr.left.left = curr.right
        curr.left = None
        curr.right = None
        return leftans