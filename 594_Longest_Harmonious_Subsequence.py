from collections import Counter
def findLHS(nums):    
    if not nums:
        return 0    
    count = Counter(nums)
    keys = list(count.keys())
    values = list(count.values())
    pool = []
    for i in range (len(keys)):
        min_number = keys[i]
        max_number = min_number+1
        if min_number+1 in keys:
            length = values[i]+values[keys.index(max_number)]
            pool.append(length)
    if not pool:
        return 0
    else:
        return max(pool)
print(findLHS(nums=[1,2,2,3,4,5,1,1,1,1]))