class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        out=[]
        for i in range(len(nums)):
            if nums[i]>0:
                out.append(i+1)
        return out