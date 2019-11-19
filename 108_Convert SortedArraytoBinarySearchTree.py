# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
    
        def helper(left,right):
            if left>right:
                return None

            mid = (right+left)//2

            root = TreeNode(nums[mid])
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        
        return helper(0,len(nums)-1)
        