class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        while n>0:
            s+=n%2
            n=n/2
        return s