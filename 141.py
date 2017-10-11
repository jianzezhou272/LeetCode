# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        else:
            slow=head
            fast=head.next
            while fast!=slow:
                if not fast.next or not fast.next.next:
                    return False
                else:
                    fast=fast.next.next
                    slow=slow.next
            return True