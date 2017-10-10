# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
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
            tra=[[0,0]]
            for i in range(n-1):
                tra.append([0,0])
            def exp(root,n):
                if not root:
                    return
                else:
                    tra[n-1][0]+=root.val
                    tra[n-1][1]+=1
                    if root.left:
                        exp(root.left,n-1)
                    if root.right:
                        exp(root.right,n-1)
                    return
            exp(root,n)
            ave=[]
            for i in range(n):
                ave.append(float(tra[n-i-1][0])/float(tra[n-i-1][1]))
            return ave