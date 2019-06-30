class Solution:
    '''
    #O(n^3)
    def is_palindromic(self, string):
        length = len(string)
        start = 0; end = length-1;
        left = string[start]; right = string[end];
        while left == right:
            if start == end or (end-start)==1:
                return True
            else:
                start += 1;
                end -= 1;
                left = string[start];
                right = string[end];
        return False
    
    def countSubstrings(self, s: str) -> int:
        if not s:
            return ""
        count = 0
        for string_length in range(len(s)):
            string_length += 1;
            for location in range(len(s)-string_length+1):
                string = s[location:location+string_length]
                if self.is_palindromic(string)==True:
                    count += 1
        return int(count)
    '''
    #O(n^2)
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        count = len(s)        
        for start in range(len(s)):
            for end in range(start+1,len(s)):
                if s[start]==s[end] and s[start:end+1]==s[start:end+1][::-1]:
                    count += 1
        return int(count)
            