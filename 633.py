class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a=0
        while 2*a**2<=c:
            if (int((c-a**2)**0.5))**2==c-a**2:
                return True
            a+=1
        return False