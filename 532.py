class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mapn = {}
        for n in nums:
            try:
                mapn[n] += 1
            except:
                mapn[n] = 1
        s = 0
        if k == 0:
            for m in mapn:
                s += int(mapn[m] >= 2)
        elif k > 0:
            for m in mapn:
                if mapn.get(m - k):
                    s += 1
                if mapn.get(m + k):
                    s += 1
            s /= 2
        return s

