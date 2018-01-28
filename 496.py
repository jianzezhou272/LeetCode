class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        out=[]
        for n in findNums:
            i=nums.index(n)
            while nums[i]<=n and i<len(nums)-1:
                i+=1
            if nums[i]>n:
                out.append(nums[i])
            else:
                out.append(-1)
        return out