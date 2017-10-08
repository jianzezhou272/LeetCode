class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        else:
            dic={1:prices[0]}
            p=max(prices[1]-prices[0],0)
            for i in range(2,len(prices)):
                dic[i]=min(dic[i-1],prices[i-1])
                p=max(prices[i]-dic[i],p)
            return p