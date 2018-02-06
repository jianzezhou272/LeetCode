class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=1
        cur=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cur+=1
                l=max(l,cur)
            else:
                cur=1
        return min(l,len(nums))