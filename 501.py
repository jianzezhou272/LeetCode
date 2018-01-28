# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic={}
        def dfs(root):
            if not root:
                return
            else:
                dic[root.val]=dic.get(root.val,0)+1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        m=0
        out=[]
        for key in dic:
            if dic[key]>m:
                m=dic[key]
                out=[key]
            elif dic[key]==m:
                out.append(key)
        return out