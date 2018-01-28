class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w=1
        t=2
        while t**2<=area:
            if area%t==0:
                w=t
            t+=1
        return [area/w,w]