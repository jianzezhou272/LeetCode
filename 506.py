class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        order=sorted(nums,reverse=True)
        rank=[]
        for n in nums:
            place=order.index(n)+1
            if place==1:
                rank.append('Gold Medal')
            elif place==2:
                rank.append('Silver Medal')
            elif place==3:
                rank.append('Bronze Medal')
            else:
                rank.append(str(place))
        return rank