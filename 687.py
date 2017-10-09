# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longestDown(root):
            if not root:
                return 0
            else:
                l=1
                if root.left and root.left.val==root.val:
                    l+=longestDown(root.left)
                if root.right and root.right.val==root.val:
                    l=max(l,1+longestDown(root.right))
                return l
        if not root:
            return 0
        else:
            L=0
            if root.left and root.left.val==root.val:
                L+=longestDown(root.left)
            if root.right and root.right.val==root.val:
                L+=longestDown(root.right)
            return max(self.longestUnivaluePath(root.left),self.longestUnivaluePath(root.right),L)