class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        
        dp = [1]*len(nums)
        father = [-1]*len(nums)
        m, index = 0, -1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        father[i]=j
            if dp[i]>m:
                m=dp[i]
                index = i
        
        res=[]
        for _ in range(m):
            res.append(nums[index])
            index = father[index]
        
        return res
        