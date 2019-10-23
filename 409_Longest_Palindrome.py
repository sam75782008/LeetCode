from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        pool = Counter(s)
        number = list(pool.values())
        ans = 0
        odd = 0
        for i in range(len(number)):
            if number[i]%2==0:
                ans = ans + number[i]
            else:
                ans = ans + number[i]-1
                odd+=1
        if odd>0:
            ans+=1
        return ans
        