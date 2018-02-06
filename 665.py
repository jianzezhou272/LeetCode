class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drop = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if drop == 1:
                    return False
                elif i == len(nums) - 1 or i == 1:
                    drop += 1
                elif nums[i - 2] <= nums[i] or nums[i - 1] <= nums[i + 1]:
                    drop += 1
                else:
                    return False
        return True
