class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        pointer= 1
        pointer_2 = 1
        
        while pointer<len(nums):
            if nums[pointer] != nums[pointer-1]:
                nums[pointer_2] = nums[pointer]
                pointer_2 += 1
            pointer+=1
        return pointer_2
                