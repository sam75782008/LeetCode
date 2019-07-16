# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        
        count = 0
        curr = head
        # findout the length of the linked list
        while curr:
            curr = curr.next
            count+=1
        #remove last one
        if n == 1:
            if count -1 == 0:
                return None
            else:
                curr = head
                for i in range(count-2):
                    curr = curr.next
                curr.next = None
                return head
        #remove first one
        elif count - n == 0:
            head = head.next
            return head
        else:
            curr = head
            for i in range(count-n-1):
                curr = curr.next
            curr.next = curr.next.next
            return head