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
        if not l1 and l2:
            return ""
        
        l1_pool = []
        temp_1 = l1
        l2_pool = []
        temp_2 = l2
        
        while temp_1:
            node = temp_1.val
            l1_pool.append(int(node))
            temp_1 = temp_1.next

        while temp_2:
            node = temp_2.val
            l2_pool.append(int(node))
            temp_2 = temp_2.next        
        a = 0
        b = 0
        for i in range(len(l1_pool)):
            a += 10**(i)*l1_pool[i]
        for j in range(len(l2_pool)):
            b += 10**(j)*l2_pool[j]
        target = list(str(a+b))[::-1]
        dummy = ListNode(0)
        tail = dummy
        for i in range(len(target)):
            tail.next = ListNode(int(target[i]))
            tail = tail.next
        
        return dummy.next
        
            
        