class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        n=0
        g=sorted(g)
        s=sorted(s)
        while len(g)>0 and len(s)>0:
            if g[0]<=s[0]:
                n+=1
                s.pop(0)
                g.pop(0)
            else:
                s.pop(0)
        return n