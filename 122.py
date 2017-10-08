class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p=0
        if len(prices)<=1:
            return p
        else:
            for i in range(1,len(prices)):
                p+=max(0,prices[i]-prices[i-1])
        return p