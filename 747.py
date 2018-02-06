class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        idx=nums.index(m)
        nums.pop(idx)
        return idx if nums==[] or m>=2*max(nums) else -1