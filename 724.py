class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        i=0
        r=sum(nums[1:])
        while l!=r and i<len(nums)-1:
            l+=nums[i]
            r-=nums[i+1]
            i+=1
        return i if nums!=[] and l==r else -1