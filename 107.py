# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dep(root):
            if not root:
                return 0
            else:
                return 1+max(dep(root.left),dep(root.right))
        n=dep(root)
        if n==0:
            return []
        else:
            tra=[[]]
            for i in range(n-1):
                tra.append([])
            def exp(root,n):
                if not root:
                    return
                else:
                    tra[n-1].append(root.val)
                    if root.left:
                        exp(root.left,n-1)
                    if root.right:
                        exp(root.right,n-1)
                    return
            exp(root,n)
            return tra