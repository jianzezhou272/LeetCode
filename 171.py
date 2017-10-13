class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        L='*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        C=0
        for ls in s:
            C*=26
            C+=L.index(ls)
        return C