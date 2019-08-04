from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dic = Counter(s)
        t_dic = Counter(t)
        
        if s_dic != t_dic:
            return False
        else:
            return True
        