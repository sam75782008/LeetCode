class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        string_length = len(s)
        pool = []
        for start in range(string_length):
            for end in range(string_length-1,-1,-1):
                if s[start]==s[end] and s[start:end+1]==s[start:end+1][::-1]:
                    pool.append(s[start:end+1])
                else:
                    pass
        
        if not pool:
            return ""
        else:
            return max(pool,key=len)