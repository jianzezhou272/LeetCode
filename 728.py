class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSDN(num):
            for d in str(num):
                if int(d)==0 or num%int(d)!=0:
                    return False
            return True
        out=[]
        for i in range(left, right+1):
            if isSDN(i):
                out.append(i)
        return out