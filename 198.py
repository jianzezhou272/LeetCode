class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={0:0}
        if len(nums)>0:
            dic[1]=max(0,nums[0])
            for i in range(2,len(nums)+1):
                dic[i]=max(dic[i-1],dic[i-2]+nums[i-1])
        return dic[len(nums)]