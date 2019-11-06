# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        if not root:
            return []
        
       
        result = []
        self.dfs(root, 0, [], sum,result)
        
        return result
        
    def dfs(self, root, nowsum, path, target, result):
        
        if not root:
            return
        
        nowsum += root.val
        path.append(root.val)
        
        if not root.left and not root.right:
            if nowsum == target:
                result.append(path[:])
               
        self.dfs(root.left, nowsum, path, target, result)
        self.dfs(root.right, nowsum, path, target, result)
        path.pop()
        