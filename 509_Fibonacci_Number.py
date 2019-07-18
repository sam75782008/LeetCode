class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        elif N==1:
            return 1
        else:
            res = [0,1]
            for i in range(2,N+1):
                res.append(res[-1]+res[-2])
            return res[-1]