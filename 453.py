class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=min(nums)
        s=0
        for n in nums:
            s+=n-x
        return s