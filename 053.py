class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        dic[0]=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            dic[i]=max(dic[i-1]+nums[i],nums[i])
            maxi=max(maxi,dic[i])
        return maxi