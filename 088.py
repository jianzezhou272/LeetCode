class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        s=0
        t=0
        nums1=nums1[:m]
        while s<m and t<n:
            if nums1[s]>nums2[t]:
                nums1=nums1[0:s]+[nums2[t]]+nums1[s:]
                t+=1
            else:
                s+=1
        if t<n:
            nums1=nums1+nums2[t:]
#wrong

#in place
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        m-=1
        n-=1
        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[m+n+1]=nums1[m]
                m-=1
            else:
                nums1[m+n+1]=nums2[n]
                n-=1
        if n>=0:
            nums1[:n+1]=nums2[:n+1]
