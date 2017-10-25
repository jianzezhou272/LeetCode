class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0 or k==0:
            return 0
        else:
            way={0:1,1:k,2:k**2}
            for i in range(3,n+1):
                way[i]=(k-1)*way[i-1]+(k-1)*way[i-2]
            return way[n]