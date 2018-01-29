# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumT(root):
            if not root:
                return 0
            else:
                return root.val+sumT(root.left)+sumT(root.right)
        if not root:
            return 0
        else:
            return abs(sumT(root.left)-sumT(root.right))+self.findTilt(root.left)+self.findTilt(root.right)