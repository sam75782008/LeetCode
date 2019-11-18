class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums)==1:
            return nums[0]
        curr_sum = max_sum = nums[0]
        
        for i in range(1,len(nums)):
            curr_sum = max(nums[i],curr_sum+nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
        
        
        
        
        