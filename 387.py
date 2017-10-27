class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}
        for i in range(len(s)):
            if dic.get(s[i])>=0:
                dic[s[i]].append(i)
            else:
                dic[s[i]]=[i]
        mini=len(s)
        for key in dic:
            if len(dic[key])==1:
                mini=min(mini,dic[key][0])
        return mini if mini<len(s) else -1