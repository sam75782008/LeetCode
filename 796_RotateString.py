class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        
        n = len(A)
        m = len(B)
        
        if n != m:
            return False
        
        for i in range(1,n):
            offset = i
            check = A[offset:]+A[:offset]
            if check == B:
                return True
        return False
        