# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        dummy1 = head1 = ListNode(None)
        dummy2 = head2 = ListNode(None)
        curr1 = head
        while curr1:
            if curr1.val<x:
                dummy1.next = curr1
                dummy1 = dummy1.next
            else:
                dummy2.next = curr1
                dummy2 = dummy2.next
            curr1 = curr1.next
        dummy2.next = None
        dummy1.next = head2.next
        return head1.next
