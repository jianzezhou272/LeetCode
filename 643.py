class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sm=sum(nums[:k])
        dif=0
        for i in range(k,len(nums)):
            dif+=(nums[i]-nums[i-k])
            if dif>0:
                sm+=dif
                dif=0
        return sm*1.0/k