class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic={}
        for ls in s:
            try:
                dic[ls]+=1
            except:
                dic[ls]=1
        for lt in t:
            if not dic.get(lt) or dic[lt]==0:
                return lt
            else:
                dic[lt]-=1