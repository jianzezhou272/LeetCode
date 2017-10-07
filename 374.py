# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L=0
        H=n+1
        M=(1+n)/2
        while L<H:
            if guess(M)==0:
                return M
            elif guess(M)==1:
                L = max(L+1,M)
                M = (L+H)/2
            else:
                H = min(H-1,M)
                M = (L+H)/2
        return M