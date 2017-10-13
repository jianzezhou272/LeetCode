class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        for i in range(n):
            l.append(1)
        if n>0:
            l[0]=0
            if n>1:
                l[1]=0
                fac=2
                while fac**2<=n:
                    ind=fac**2
                    while ind<n:
                        l[ind]=0
                        ind+=fac
                    fac+=1
                    while l[fac]==0:
                        fac+=1
            return sum(l)
        return 0