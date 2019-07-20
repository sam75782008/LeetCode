# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return ""
        
        q = Queue()
        q.put(root)
        res = []
        while not q.empty():
            pool = []
            length = q.qsize()
            for i in range(length):
                curr = q.get()
                pool.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            res.append(pool)
        
        return res[::-1]
        
        