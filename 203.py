# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        fakehead = ListNode(0)
        fakehead.next = head
        node = fakehead
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return fakehead.next

