class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mi=min(arrays[0])
        ma=max(arrays[0])
        dis=0
        for l in arrays[1:]:
            dis=max(dis,max(l)-mi,ma-min(l))
            mi=min(min(l),mi)
            ma=max(max(l),ma)
        return dis