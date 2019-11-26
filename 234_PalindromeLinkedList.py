# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        ans = []
        curr = head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        if len(ans)==1:
            return True
        return ans==ans[::-1]
    
        