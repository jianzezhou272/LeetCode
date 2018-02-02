class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for n in nums:
            dic[n]=dic.get(n,0)+1
        m=0
        for key in dic:
            if dic.get(key) and dic.get(key-1):
                m=max(m,dic[key]+dic[key-1])
        return m