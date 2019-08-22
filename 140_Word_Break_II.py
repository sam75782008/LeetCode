class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        return self.dfs(s,wordDict,memo)
    
    def dfs(self,s,word_dict,memo):
        if len(s) ==0:
            return []
        if s in memo:
            return memo[s]
        
        partitions = []
        
        if s in word_dict:
            partitions.append(s)
        for i in range(1,len(s)):
            word = s[:i]
            if word not in word_dict:
                continue
            sub_partitions = self.dfs(s[i:],word_dict,memo)
            for sub_partition in sub_partitions:
                partitions.append(word + " " + sub_partition)
        memo[s] = partitions
        return partitions        