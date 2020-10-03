# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        queue = collections.deque([root])
        
        depth = 1
        while queue:
            
            for _ in range(len(queue)):
                root = queue.popleft()
                
                if not root.left and not root.right:
                    return depth
                else:
                    queue.append(root.left) if root.left else None
                    queue.append(root.right) if root.right else None
            
            depth += 1
        
            