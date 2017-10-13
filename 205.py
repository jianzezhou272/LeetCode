class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            dic = {}
            for i in range(len(s)):
                try:
                    if dic[s[i]] != t[i]:
                        return False
                except:
                    dic[s[i]] = t[i]
            DIC = {}
            for j in range(len(t)):
                try:
                    if DIC[t[j]] != s[j]:
                        return False
                except:
                    DIC[t[j]] = s[j]
            return True
