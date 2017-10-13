class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str=str.split()
        if len(pattern)!=len(str):
            return False
        else:
            P={}
            for i in range(len(pattern)):
                try:
                    if P[pattern[i]]!=str[i]:
                        return False
                except:
                    P[pattern[i]]=str[i]
            S={}
            for j in range(len(str)):
                try:
                    if S[str[j]]!=pattern[j]:
                        return False
                except:
                    S[str[j]]=pattern[j]
            return True