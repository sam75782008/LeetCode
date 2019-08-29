# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.out = []
        self.helper(root)
        return self.out
    
    def helper(self, curr):
        if not curr:
            return
        self.helper(curr.left)
        self.out.append(curr.val)
        self.helper(curr.right)