class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        o=''
        start=0
        while start<len(s):
            mid=min(start+k,len(s))
            end=min(start+2*k,len(s))
            if start==0:
                o+=s[mid-1::-1]
            else:
                o+=s[mid-1:start-1:-1]
            o+=s[mid:end]
            start+=2*k
        return o