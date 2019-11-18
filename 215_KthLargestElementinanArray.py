import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        pool = []
        for i in range(len(nums)):
            heapq.heappush(pool,nums[i])
            if len(pool)>k:
                heapq.heappop(pool)
        return pool[0]
        