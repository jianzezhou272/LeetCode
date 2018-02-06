class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res=n%2
        n=n/2
        while n>0:
            if n%2!=(1-res):
                return False
            else:
                res=1-res
                n=n/2
        return True