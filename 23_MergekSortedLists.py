import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

ListNode.__lt__ = lambda x,y:(x.val<y.val)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        heap=[]
        for head in lists:
            if head:
                heapq.heappush(heap,head)
        
        while heap:
            head = heapq.heappop(heap)
            tail.next = head
            tail = head
            if head.next:
                heapq.heappush(heap,head.next)
        
        return dummy.next