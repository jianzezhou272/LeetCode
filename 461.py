class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z=x^y
        s=0
        while z>0:
            s+=z%2
            z/=2
        return s