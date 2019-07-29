class Solution:
    def numDecodings(self, s: str) -> int:
		if not s:
			return 0
        number = list(s)
        if len(number)==1 and int(s[0]) != 0:
            return 1
        elif len(number)==1 and int(s[0]) == 0:
            return 0
        elif int(s[0])==0:
            return 0
        else:
            res = []
            res.append(1) #0 position
            res.append(1) #1 position
            for i in range(1,len(number)):
                if (int(number[i])!=0) and (10<=(int(number[i-1])*10+int(number[i]))<=26):
                    answer = res[-2]+res[-1]
                    res.append(answer)
                elif (int(number[i])!=0) and (int(number[i-1])!=0 or 10>(int(number[i-1])*10+int(number[i])) or (int(number[i-1])*10+int(number[i]))>26):
                    answer = res[-1]
                    res.append(answer)
                elif (int(number[i])==0) and (10<=(int(number[i-1])*10+int(number[i]))<=26):
                    answer = res[-2]
                    res.append(answer)
                else:
                    return 0
        return res[-1]
                
        