# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.res = []
        self.helper(root)
        
        for i in range(1,len(self.res)):
            if self.res[i]<=self.res[i-1]:
                return False        
        return True
    
    def helper(self,root):
        if not root:
            return
        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)