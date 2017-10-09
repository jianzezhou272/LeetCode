class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        while n>4:
            n/=5
            s+=n
        return s