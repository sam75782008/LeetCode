import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_dict = collections.Counter(deadends)
        if '0000' in dead_dict:
            return -1
        first = '0000'
        q = collections.deque()
        vistted = {}
        q.append(first)
        vistted[first] = 1
        
        res = 0
        while q:
            size = len(q)
            res += 1
            for _ in range(size):
                current = q.popleft()
                if current == target:
                    return res-1
                for nextPwd in self.getnextPwd(current):
                    if nextPwd in dead_dict or nextPwd in vistted:
                        continue
                    else:
                        vistted[nextPwd] = 1
                        q.append(nextPwd)
        return -1
        
    def getnextPwd(self, pwd):
        pwds = []
        for i in range(4):
            left, right = pwd[:i], pwd[i+1:]
            if int(pwd[i])-1<0:
                pre = 9
            else:
                pre = int(pwd[i])-1
            if int(pwd[i])+1>9:
                nex = 0
            else:
                nex = int(pwd[i])+1
            pool1 = left+str(pre)+right
            pool2 = left+str(nex)+right
            pwds.append(pool1)
            pwds.append(pool2)
        return pwds
                    