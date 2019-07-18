# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root,height=1)
        return self.res
        
    
    def helper(self,root,height):
        if not root:
            return
        
        self.res = max(self.res,height)
        
        self.helper(root.left,height+1)
        self.helper(root.right,height+1)