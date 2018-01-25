class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        s=0
        for p in points:
            dist={}
            for q in points:
                d=(p[0]-q[0])**2+(p[1]-q[1])**2
                if dist.get(d):
                    dist[d]+=1
                else:
                    dist[d]=1
            for key in dist:
                s+=dist[key]*(dist[key]-1)
        return s