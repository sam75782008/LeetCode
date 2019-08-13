from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return []
        leng_p = len(p)
        ans = Counter(p)
        leng_s = len(s)
        res = []
        for i in range(leng_s):
            if i+leng_p>leng_s:
                break
            elif i == 0:
                target = s[i:i+leng_p]
                temp = Counter(target)
            else:
                temp[s[i-1]] -= 1
                if temp[s[i-1]] == 0:
                    del temp[s[i-1]]
                if s[i+leng_p-1] in temp:
                    temp[s[i+leng_p-1]] += 1
                else:
                    temp[s[i+leng_p-1]] = 1
            if temp == ans:
                res.append(i)                
        return res
        