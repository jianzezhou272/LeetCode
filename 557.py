class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        out=[]
        s=s.split()
        for w in s:
            out.append(w[::-1])
        return ' '.join(out)