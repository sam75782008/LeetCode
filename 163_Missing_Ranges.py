class Solution:
    def helper(self, left_point, right_point):
        if left_point == right_point:
            return str(left_point)
        else:
            return str(left_point) + "->" + str(right_point)
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if len(nums) == 0:
            ans.append(self.helper(lower, upper))
            return ans
        pre_point = lower - 1
        for point in nums:
            if pre_point != point and pre_point + 1 != point:
                ans.append(self.helper(pre_point + 1, point - 1))
            pre_point = point
        if nums[-1] < upper:
            ans.append(self.helper(nums[-1] + 1, upper))
        return ans
                
                
        