# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        i,j = 0,0
        slow = head
        while head.next:
            slow = slow.next
            head = head.next
            if head.next:
                head = head.next
        return slow
            
            