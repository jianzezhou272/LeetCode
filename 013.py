class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=0
        for i in range(len(s)):
            if s[i]=='M':
                n+=1000
            elif s[i]=='D':
                n+=500
            elif s[i]=='C':
                if i<len(s)-1 and s[i+1] in 'DM':
                    n-=100
                else:
                    n+=100
            elif s[i]=='L':
                n+=50
            elif s[i]=='X':
                if i<len(s)-1 and s[i+1] in 'CL':
                    n-=10
                else:
                    n+=10
            elif s[i]=='V':
                n+=5
            else:
                if i<len(s)-1 and s[i+1] in 'VX':
                    n-=1
                else:
                    n+=1
        return n
