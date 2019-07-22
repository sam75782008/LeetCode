class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return ""
        
        if len(intervals)==1:
            return intervals
        
        intervals = sorted(intervals, key = lambda x: int(x[0]));
        res=[]
        i=0
        while i <(len(intervals)-1):
            if not res:
                curr_item = intervals[i]
                curr_next = intervals[i+1]
                if curr_item[-1]>=curr_next[0]:
                    res.append([curr_item[0],max(curr_item[-1],curr_next[-1])])
                else:
                    res.append(curr_item)
                    res.append(curr_next)
                i += 1
            else:
                curr_item = res[-1]
                curr_next = intervals[i+1]
                if curr_item[1]>=curr_next[0]:
                    res.pop()
                    res.append([curr_item[0],max(curr_item[-1],curr_next[-1])])
                else:
                    res.append(curr_next)
                i += 1
        return res