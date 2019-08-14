from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pool = Counter(nums)
        max_len = 0
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                continue
            else:
                mins = nums[i]-1
                plus = nums[i]+1
                while mins in pool or plus in pool:
                    if mins in pool:
                        if mins not in res:
                            res[mins]=1
                        mins -= 1
                    if plus in pool:
                        if plus not in res:
                            res[plus]=1
                        plus += 1
                max_len = max((plus-mins-1),max_len)
        return max_len