class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1={}
        for n1 in nums1:
            try:
                map1[n1]+=1
            except:
                map1[n1]=1
        intsec=[]
        for n2 in nums2:
            if map1.get(n2) and map1[n2]>0:
                map1[n2]-=1
                intsec.append(n2)
        return intsec