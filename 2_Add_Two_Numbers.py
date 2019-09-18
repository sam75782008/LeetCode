from collections import deque
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.l1_list=deque()
        self.l2_list=deque()
        self.helper1(l1)
        self.helper2(l2)
        
        number1 = int("".join(list(self.l1_list)))
        number2 = int("".join(list(self.l2_list)))
        result = number1+number2
        res = [int(x) for x in str(result)] 
        
        dummy = ListNode(0)
        output = ListNode(int(res.pop()))
        dummy.next = output
        while res:
            temp = ListNode(int(res.pop()))
            output.next = temp
            output = output.next
        
        return dummy.next 

    
    def helper1(self,curr1):
        if not curr1:
            return
        self.l1_list.appendleft(str(curr1.val))
        self.helper1(curr1.next)
        return

    def helper2(self,curr2):
        if not curr2:
            return
        self.l2_list.appendleft(str(curr2.val))
        self.helper2(curr2.next)
        return