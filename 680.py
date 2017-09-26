class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        head=0
        tail=len(s)-1
        while head<tail:
            if s[head]==s[tail]:
                head+=1
                tail-=1
            else:
                return s[head:tail]==s[head:tail][::-1] or s[head+1:tail+1]==s[head+1:tail+1][::-1]
        return True