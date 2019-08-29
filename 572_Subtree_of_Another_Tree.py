# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s and t:
            return False
        if s and not t:
            return True
        preorder_s = self.helper(s)
        preorder_t = self.helper(t)
        
        return preorder_t in preorder_s
    
    def helper(self,curr):
        if not curr:
            return "None"
        
        output = '#'+str(curr.val)+' '+self.helper(curr.left)+' '+self.helper(curr.right)
        return output