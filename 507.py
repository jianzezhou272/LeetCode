class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        if num>1:
            fac=[]
            t=2
            while t**2<num:
                if num%t==0:
                    fac.append(t)
                t+=1
            s=1+sum(fac)
            for f in fac:
                s+=num/f
            if t**2==num:
                s+=t
            return s==num