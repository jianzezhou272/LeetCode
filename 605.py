class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        e=0
        f=0
        flowerbed=[0]+flowerbed+[0,1]
        for sp in flowerbed:
            print e,f
            if sp==0:
                e+=1
            else:
                f+=max((e-1)/2,0)
                e=0
        return f>=n