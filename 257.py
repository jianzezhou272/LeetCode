# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            p=self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)
            for i in range(len(p)):
                p[i]=str(root.val)+'->'+p[i]
            return p