class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            res = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == res:
                    out.append(i)
                    out.append(j)
                    return out