# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def lenth(head):
            l = 0
            while head:
                l += 1
                head = head.next
            return l

        la = lenth(headA)
        lb = lenth(headB)
        if la > lb:
            for i in range(la - lb):
                headA = headA.next
        else:
            for i in range(lb - la):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        if headA:
            return headA
        else:
            return