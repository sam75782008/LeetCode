import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return None
        ans = []
        '''#general O(n^2)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ans.append([nums1[i],nums2[j]])
        ans = sorted(ans, key=lambda x:x[0]+x[1])
        return ans[:k]
        '''
        h = [(nums1[0]+nums2[0],0,0)]
        visted = set()
        
        while len(ans)<k and h:
            val, i, j = heapq.heappop(h)
            ans.append((nums1[i],nums2[j]))
            
            if i+1<len(nums1) and (i+1,j) not in visted:
                heapq.heappush(h, (nums1[i+1]+nums2[j],i+1,j))
                visted.add((i+1,j))
            if j+1<len(nums2) and (i,j+1) not in visted:
                heapq.heappush(h, (nums1[i]+nums2[j+1],i,j+1))
                visted.add((i,j+1))
        
        return ans