# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        pointerfirst = head
        pointersecond = head
        
        while pointerfirst and pointerfirst.next:
            if pointersecond==pointerfirst.next:
                return True
            else:
                pointersecond = pointersecond.next
                pointerfirst = pointerfirst.next.next
        return False
        
        