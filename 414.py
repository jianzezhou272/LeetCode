class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(list(set(nums)),reverse=True)
        try:
            return nums[2]
        except:
            return nums[0]