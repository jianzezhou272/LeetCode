class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        intg=''
        for d in digits:
            intg+=str(d)
        intg=str(int(intg)+1)
        intg=list(intg)
        for i in range(len(intg)):
            intg[i]=int(intg[i])
        return intg