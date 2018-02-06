class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last=0
        cur=1
        sm=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cur+=1
                if cur<=last:
                    sm+=1
            else:
                last=cur
                cur=1
                sm+=1
        return sm