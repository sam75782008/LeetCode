class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0.0:
            return 0
        if n==0:
            return 1
        if n<0:
            n = -n
            x = 1/x
        
        ans = 1.0; temp = x
        
        while n != 0:
            if (n%2==1.0):
                ans *= temp
            temp *= temp
            n //=2
        return ans