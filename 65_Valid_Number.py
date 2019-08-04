class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            s = float(s)
            return True
        except:
            return False
        '''
        if not s:
            return False
        
        l, r = 0, len(s)-1
        while l<=r and s[l]==" ":
            l+=1
        while l<=r and s[r]==" ":
            r-=1
        if l>r:
            return False
        if s[l] in "+-":
            l+=1
        if l>r:
            return False
            
        dot, exp = -1, -1
        for i in range(l,r+1):
            if s[i] in "1234567890":
                continue
            if s[i] == '.':
                if dot>=0:
                    return False #two float point
                else:
                    dot = i
            elif s[i] in 'eE':
                if exp >=0:
                    return False #two exponential
                else:
                    exp = i
            else:
                return False #abc...
        
        if exp == l or exp == r:
            return False
        if dot>exp:
            return False
        if dot == l:
            return dot<r and s[dot+1] in '1234567890'
        if dot == r:
            return l<dot and s[dot-1] in '1234567890'
        return True
        '''
        
        