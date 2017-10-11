class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k=1
        pa=[1]
        for i in range(1,rowIndex+1):
            k=k*(rowIndex-i+1)/i
            pa.append(k)
        return pa