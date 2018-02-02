class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        a=0
        for n in nums:
            a+=len(n)
        if a!=r*c:
            return nums
        else:
            out=[]
            rr=0
            cc=0
            for i in range(r):
                out.append([])
                for j in range(c):
                    out[i].append(nums[rr][cc])
                    if cc>=len(nums[rr])-1:
                        cc=0
                        rr+=1
                    else:
                        cc+=1
            return out