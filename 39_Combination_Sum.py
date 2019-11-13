class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        results=[]
        self.dfs(candidates, target, 0, [], results)
        return results
    
    
    def dfs(self, candidates, target, start, combination, results):
        if target < 0:
            return
        if target == 0:
            return results.append(list(combination)) #深拷貝
        
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            combination.pop()#前次答案不行，去掉
        