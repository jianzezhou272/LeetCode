class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        m=sys.maxint
        o=[]
        for l in list1:
            if l in list2:
                s=list1.index(l)+list2.index(l)
                if s<=m:
                    m=s
                    o.append(l)
        return o