class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        res = {}
        for i in range(len(dict)):
            target = dict[i]
            p = 0
            while len(target)-p>3:
                abbre = self.helper(target,p)
                if abbre not in res:
                    res[abbre] = 1
                else:
                    res[abbre] += 1
                p += 1
            if target not in res:
                res[target] = 1
            else:
                res[target] += 1
        for i in range(len(dict)):
            target = dict[i]
            p = 0
            while len(target)-p>3:
                new = self.helper(target,p)
                if res[new] == 1:
                    dict[i] = new
                    break
                else:
                    p += 1
        return dict
    
    def helper(self,s,p):
        if (len(s)-p)<=3:
            return s
        else:
            return s[:p+1]+str(len(s)-p-2)+s[-1]
        