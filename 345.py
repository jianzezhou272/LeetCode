class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow=[]
        o=''
        for l in s:
            if l in 'aeiouAEIOU':
                vow.append(l)
        for l in s:
            if l not in 'aeiouAEIOU':
                o+=l
            else:
                o+=vow.pop()
        return o
"""
time exceed
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        start=0
        end=len(s)-1
        vow='aeiouAEIOU'
        while start<end:
            while start<end and s[start] not in vow:
                start+=1
            while end>start and s[end] not in vow:
                end-=1
            b=s[start]
            s[start]=s[end]
            s[end]=b
            start+=1
            end-=1
        return ''.join(s)