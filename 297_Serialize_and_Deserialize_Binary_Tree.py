from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        self.out = ""
        self.ser_helper(root)
        return self.out
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        check_list = deque(data.split(','))
        if len(check_list)==0 or check_list[0]=='None':
            return None
        root = self.dser_helper(check_list)
        return root       

    def ser_helper(self,curr):
        if not curr:
            self.out+='None,'
            return
        self.out+=str(curr.val)+','
        self.ser_helper(curr.left)
        self.ser_helper(curr.right)
    
    def dser_helper(self,node):
        if node[0]=='None':
            node.popleft()
            return None
        drop = node.popleft()
        root = TreeNode(drop)
        root.left = self.dser_helper(node)
        root.right = self.dser_helper(node)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))