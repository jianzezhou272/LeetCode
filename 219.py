class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for i in range(len(nums)):
            if dic.get(nums[i])==None:
                dic[nums[i]]=i
            elif i-dic[nums[i]]<=k:
                return True
            else:
                dic[nums[i]]=i
        return False