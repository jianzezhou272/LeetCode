# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rootval=[]
        def bfs(root):
            if not root:
                return
            else:
                bfs(root.left)
                rootval.append(root.val)
                bfs(root.right)
        bfs(root)
        rootval=sorted(list(set((rootval))))
        if len(rootval)<=1:
            return -1
        else:
            return rootval[1]