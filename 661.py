class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        A = []
        L = len(M)
        W = len(M[0])
        for i in range(L):
            A.append([])
            for j in range(W):
                c = 0
                aij = 0
                for k in range(max(0, i - 1), min(L, i + 2)):
                    for l in range(max(0, j - 1), min(W, j + 2)):
                        aij += M[k][l]
                        c += 1
                A[i].append(aij / c)
        return A
