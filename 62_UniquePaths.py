class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.dfs(0, 0, m-1, n-1, {})
    
      
    def dfs(self, i, j, m, n, memo):
        if i == m or j ==n:
            return 1
        if (i,j) in memo:
            return memo[(i,j)]
        
        ans = 0
        ans += self.dfs(i+1, j, m, n,memo)
        ans += self.dfs(i, j+1, m, n,memo)
        memo[(i,j)] = ans
        return ans