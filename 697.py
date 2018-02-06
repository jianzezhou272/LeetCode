class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = {}
        right = {}
        count = {}
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i + 1
            count[nums[i]] = count.get(nums[i], 0) + 1

        m = max(count.values())
        l = len(nums)
        for n in count:
            if count[n] == m:
                l = min(l, right[n] - left[n])
        return l