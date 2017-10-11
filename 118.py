class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        else:
            pa=[[1]]
            for n in range(1,numRows):
                l1=[0]+pa[n-1]
                l2=pa[n-1]+[0]
                pa.append([])
                for i in range(n+1):
                    pa[n].append(l1[i]+l2[i])
            return pa        