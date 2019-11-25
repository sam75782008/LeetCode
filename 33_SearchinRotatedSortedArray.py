class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[left]:
                if nums[mid]>target and target>=nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target and nums[right]>=target:
                    left = mid+1
                else:
                    right = mid-1
        return -1
        