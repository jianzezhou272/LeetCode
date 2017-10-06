# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l=[]
        while l1 or l2:
            if not l1 or (l2 and l2.val<l1.val):
                l.append(l2.val)
                l2=l2.next
            else:
                l.append(l1.val)
                l1=l1.next
        return l
