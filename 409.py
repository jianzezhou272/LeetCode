class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=0
        st=list(set(s))
        s=list(s)
        for l in st:
            n+=2*(s.count(l)/2)
        return min(n+1,len(s))