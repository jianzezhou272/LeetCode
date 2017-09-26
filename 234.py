# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def exp(head):
            s=[]
            while head:
                s.append(head.val)
                head=head.next
            return s
        s=exp(head)
        return s==s[::-1]

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        else:
            slow=head
            fast=head
            while fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
        slow=slow.next
        node=None
        while slow:
            nxt=slow.next
            slow.next=node
            node=slow
            slow=nxt
        while node:
            if node.val!=head.val:
                return False
            else:
                node=node.next
                head=head.next
        return True