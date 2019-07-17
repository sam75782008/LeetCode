class Solution:
    def isValid(self, s: str) -> bool:
        #if not s or len(s)==0:
        #    return False
        
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i]==')' or s[i]=='}' or s[i]==']':
                if not stack:
                    return False
                else:
                    a = stack.pop()
                    if s[i]==')' and a == '(':
                        continue
                    elif s[i]=='}' and a == '{':
                        continue
                    elif s[i]==']' and a == '[':
                        continue
                    else:
                        return False
                    
        if not stack:
            return True
        else:
            return False