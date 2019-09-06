from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        if not root.right and not root.left:
            return root
        self.out = deque()
        self.helper(root)
        self.out.popleft()
        #re-create the tree based on the value
        curr = root
        while self.out:
            pop = self.out.popleft()
            new_node = TreeNode(pop)
            curr.left = None
            curr.right = new_node
            curr = curr.right
            
    #pre-order to triversal all node and get values   
    def helper(self,curr):
        if not curr:
            return
        self.out.append(curr.val)
        self.helper(curr.left)
        self.helper(curr.right)
        curr.left = None
        curr.right = None

        