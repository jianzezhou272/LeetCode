# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def areSymmetric(a,b):
            if not a and not b:
                return True
            elif not a or not b:
                return False
            else:
                return a.val==b.val and areSymmetric(a.left,b.right) and areSymmetric(a.right,b.left)
        if not root:
            return True
        else:
            return areSymmetric(root.left, root.right)