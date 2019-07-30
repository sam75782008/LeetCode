class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if not abbr:
            return False
        origin = list(word)
        check = list(abbr)
        if len(check)>len(origin):
            return False
        i=0
        j=0
        while i<len(check) and j<len(origin):
            if check[i].isalpha():
                if origin[j]!=check[i]:
                    return False
                else:
                    i+=1
                    j+=1
            else:
                temp = ''
                while i<len(check) and check[i].isnumeric():
                    temp += check[i]
                    if temp =='0':
                        return False
                    i += 1
                j += int(temp)
        return i==len(check) and j==len(origin)
                    
                