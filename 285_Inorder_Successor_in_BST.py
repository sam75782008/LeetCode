# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if not p:
            return None

        if root.val<=p.val:
            return self.inorderSuccessor(root.right,p)
        else:
            leftans = self.inorderSuccessor(root.left,p)
            if not leftans:
                return root
            else:
                return leftans        