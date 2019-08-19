# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.pool = {}
        h = 0
        hleft = self.dfs(root.left,h)
        hright = self.dfs(root.right,h)
        h = max(hleft,hright)+1
        self.pool[h]=[root.val]
        return list(self.pool.values())
    
    def dfs(self,curr,height):
        if not curr:
            return height
        hleft = self.dfs(curr.left,height)
        hright = self.dfs(curr.right,height)
        newheight = max(hleft,hright)+1
        if newheight in self.pool:
            self.pool[newheight].append(curr.val)
        else:
            self.pool[newheight] = [curr.val]
        curr.left=None
        curr.right=None
        return newheight        