class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ind=0
        for n in nums:
            if n>=target:
                return ind
            else:
                ind+=1
        return ind