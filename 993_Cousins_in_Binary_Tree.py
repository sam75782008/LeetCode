# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution: 
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        self.queue = collections.deque([root])
        
        while self.queue:
            depth = len(self.queue)
            parent = False
            cousins = False

            for _ in range(depth):
                node = self.queue.popleft()

                if not node:
                    parent = False
                else:
                    if node.val == x or node.val==y:
                        if not cousins: #find first target
                            parent, cousins = True, True
                        else: #find second target, check if same parent
                            return not parent
                    #finish checking, add new children point
                    self.queue.append(node.left) if node.left else None
                    self.queue.append(node.right) if node.right else None
                    self.queue.append(None)

            #finish all leafs and only find one target
            if cousins:
                return False
        #finish all tree search
        return False