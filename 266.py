import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=collections.Counter(s)
        t=0
        for ct in c:
            if c[ct]%2==1:
                t+=1
        return t<=1