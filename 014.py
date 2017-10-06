class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=''
        if len(strs)>0:
            fir=strs[0]
            for i in range(len(fir)):
                for st in strs[1:]:
                    if i>=len(st) or st[i]!=fir[i]:
                        return s
                s+=fir[i]
        return s
