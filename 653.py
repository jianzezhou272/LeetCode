# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def expand(root):
            if not root:
                return []
            else:
                return [root.val]+expand(root.left)+expand(root.right)
        nodes=expand(root)
        for i in range(len(nodes)-1):
            if k-nodes[i] in nodes[i+1:]:
                return True
        return False