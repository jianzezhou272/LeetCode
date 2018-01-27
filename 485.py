class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur=0
        maxi=0
        for n in nums:
            if n==1:
                cur+=1
                maxi=max(maxi,cur)
            else:
                cur=0
        return maxi