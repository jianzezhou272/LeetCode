class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        head=0
        tail=len(s)-1
        while head<tail:
            if not s[head].isalnum():
                head+=1
            elif not s[tail].isalnum():
                tail-=1
            elif s[head]==s[tail]:
                head+=1
                tail-=1
            else:
                return False
        return True