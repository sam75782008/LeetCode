class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        
        return self.dfs(n,{})
        
    def dfs(self,n,memo):
        if n in memo:
            return memo[n]
        if n ==0 or n ==1:
            return 1
        ans = 0
        ans += self.dfs(n-1, memo)
        ans += self.dfs(n-2,memo)
        memo[n] = ans
        
        return ans
        
        