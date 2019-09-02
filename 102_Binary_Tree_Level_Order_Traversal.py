# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.out = {}
        height = 0
        self.out[height]=[root.val]
        self.helper(root.left,height+1)
        self.helper(root.right,height+1)
        
        return list(self.out.values())
        
    def helper(self,curr,height):
        if not curr:
            return
        if height not in self.out:
            self.out[height]=[curr.val]
        else:
            self.out[height].append(curr.val)
        self.helper(curr.left,height+1)
        self.helper(curr.right,height+1)
        