# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = 1
        U = n
        M = (L+U)/2
        while L < M:
            if isBadVersion(M):
                U = M
                M = (L+U)/2
            else:
                L = M
                M = (L+U)/2
        return M+1-int(isBadVersion(M))