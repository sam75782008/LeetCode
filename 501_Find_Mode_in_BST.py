# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pool = []
    
    def traversal(self,root):
        if not root:
            return
        
        self.pool.append(root.val)
        self.traversal(root.left)
        self.traversal(root.right)
        
        return
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.traversal(root)
        
        temp = {}
        for i in range(len(self.pool)):
            if self.pool[i] not in temp:
                temp[self.pool[i]] = 1
            else:
                temp[self.pool[i]] += 1
                
        mode = max(temp.values())
        output = []
        
        for key, value in temp.items():
            if value==mode:
                output.append(key)
                
        return output