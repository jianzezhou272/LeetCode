# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def UL(root):
            if not root:
                return [-sys.maxint,sys.maxint]
            elif root.val>target:
                return [UL(root.left)[0],min(root.val,UL(root.left)[1])]
            elif root.val<target:
                return [max(root.val,UL(root.right)[0]),UL(root.right)[1]]
            else:
                return [root.val,root.val]
        a,b = UL(root)[0],UL(root)[1]
        if target-a<b-target:
            return a
        else:
            return b