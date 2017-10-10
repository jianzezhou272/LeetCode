# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def topSum(root, sum):
            if not root:
                return 0
            else:
                return int(root.val == sum) + topSum(root.left, sum - root.val) + topSum(root.right, sum - root.val)

        if not root:
            return 0
        else:
            return topSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
