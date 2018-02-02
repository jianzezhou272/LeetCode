# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            else:
                return t1.val == t2.val and sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)

        if not s or not s.left and not s.right:
            return sameTree(s, t)
        elif not s.left:
            return sameTree(s, t) or self.isSubtree(s.right, t)
        elif not s.right:
            return sameTree(s, t) or self.isSubtree(s.left, t)
        else:
            return sameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)