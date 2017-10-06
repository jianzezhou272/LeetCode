class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i]==0:
                nums.pop(i)
                n-=1
                nums.append(0)
            else:
                i+=1