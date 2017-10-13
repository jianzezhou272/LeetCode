class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = int((2 * n) ** 0.5) - 1
        while (l + 1) * (l + 2) <= 2 * n:
            l += 1
        return l
