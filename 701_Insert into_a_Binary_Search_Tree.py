# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.helper_insert(root,val)
    
    def helper_insert(self, root,val):
        if not root:
            return TreeNode(val)
        
        if root.val<val:
            root.right = self.helper_insert(root.right,val)
        elif root.val>val:
            root.left = self.helper_insert(root.left,val)
        
        return root