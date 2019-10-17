class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        out = [0]*n
        out[0] = 1
        
        for i in range(1,n):
            out[i] = out[i-1]*nums[i-1]
        
        R = 1
        for i in reversed(range(n)):
            out[i] = out[i]*R
            R = R*nums[i]
        
        return out