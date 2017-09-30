class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        return 2*sum(s)-sum(nums)

