class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs)==0:
            return 0
        for i in range(1,len(costs)):
            for j in range(3):
                costs[i][j] = costs[i][j] + min(costs[i-1][(j+1)%3],costs[i-1][(j+2)%3])
        
        return min(costs[-1][:])
        