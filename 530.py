# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def minv(root):
            if not root.left:
                return root.val
            else:
                return minv(root.left)
        def maxv(root):
            if not root.right:
                return root.val
            else:
                return maxv(root.right)
        if root.left and root.right:
            return min(self.getMinimumDifference(root.left),self.getMinimumDifference(root.right),root.val-maxv(root.left),minv(root.right)-root.val)
        elif root.right:
            return min(self.getMinimumDifference(root.right),minv(root.right)-root.val)
        elif root.left:
            return min(self.getMinimumDifference(root.left),root.val-maxv(root.left))
        else:
            return sys.maxint