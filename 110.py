# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if not root:
                return 0
            else:
                return 1+max(depth(root.left),depth(root.right))
        if not root:
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(depth(root.left)-depth(root.right))<=1