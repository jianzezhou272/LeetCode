class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses=sorted(houses)
        heaters=sorted(heaters)
        r=0
        i=0
        j=0
        while i<len(houses) and j<len(heaters):
            #print houses[i],heaters[j]
            if abs(houses[i]-heaters[j])<=r:
                i+=1
            elif j<len(heaters)-1:
                if abs(houses[i]-heaters[j])<abs(houses[i]-heaters[j+1]):
                    r=abs(houses[i]-heaters[j])
                    i+=1
                else:
                    j+=1
            else:
                r=abs(houses[i]-heaters[j])
                i+=1
        return r