class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>99:
            s=0
            n=str(n)
            for num in n:
                s+=int(num)**2
            n=s
        l=[n]
        while n!=1:
            s=0
            n=str(n)
            for num in n:
                s+=int(num)**2
            n=s
            if n in l:
                return False
            else:
                l.append(n)
        return True