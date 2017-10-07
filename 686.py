class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a=A
        c=1
        ceil=len(B)/len(A)+2
        while c<=ceil and B not in A:
            A+=a
            c+=1
        if B in A:
            return c
        else:
            return -1