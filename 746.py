class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        p=[]
        for i in range(len(cost)+1):
            if i in [0,1]:
                p.append(0)
            else:
                p.append(min(p[len(p)-2]+cost[i-2],p[len(p)-1]+cost[i-1]))
        return p.pop()