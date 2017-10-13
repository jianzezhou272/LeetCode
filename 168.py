class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        L='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        C=''
        while n>0:
            r=(n-1)%26
            n=(n-1)/26
            C=L[r]+C
        return C