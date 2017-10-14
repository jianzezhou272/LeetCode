class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        price={-1:[0,0,0]}
        for i in range(len(costs)):
            price[i]=[0,0,0]
            price[i][0]=min(price[i-1][1],price[i-1][2])+costs[i][0]
            price[i][1]=min(price[i-1][2],price[i-1][0])+costs[i][1]
            price[i][2]=min(price[i-1][0],price[i-1][1])+costs[i][2]
        return min(price[len(costs)-1])