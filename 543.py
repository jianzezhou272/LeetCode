# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def nodeToBottom(root):
            if not root:
                return 0
            else:
                return 1+max(nodeToBottom(root.left),nodeToBottom(root.right))
        if not root:
            return 0
        else:
            return max(nodeToBottom(root.left)+nodeToBottom(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))