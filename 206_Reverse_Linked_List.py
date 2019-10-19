from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        self.decouple = deque()
        self.traversal(head)
        self.temp = ListNode(None)
        self.reconnect(self.temp)
        
        return self.temp.next
        
    def traversal(self,curr):
        if not curr:
            return
        self.decouple.append(curr.val)
        self.traversal(curr.next)

    def reconnect(self,curr):
        if not self.decouple:
            return
        a = self.decouple.pop()
        curr.next = ListNode(a)
        self.reconnect(curr.next)