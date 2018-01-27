class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        whole=''.join(S.split('-')).upper()
        r=len(whole)
        out=''
        while r>K:
            out='-'+whole[r-K:r]+out
            r-=K
        out=whole[:r]+out
        return out