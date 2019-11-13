class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        self.dfs(candidates, target, 0, 0, [], [0]*len(candidates), results)
        return results
    
    def dfs(self, candidates, target, start, now, combination, use, results):
        if now == target:
            results.append(list(combination))
            return
        
        for i in range(start, len(candidates)):
            if now + candidates[i] <= target and (i==0 or candidates[i]!=candidates[i-1] or use[i-1]==1):
                combination.append(candidates[i])
                use[i]=1
                self.dfs(candidates, target, i+1, now+candidates[i], combination, use, results)
                use[i] = 0
                combination.pop()
        
        