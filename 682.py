class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid=[]
        points=0
        for o in ops:
            try:
                p=int(o)
                valid.append(p)
                points+=p
            except:
                if o=='C':
                    points-=valid.pop()
                elif o=='D':
                    p=2*valid[len(valid)-1]
                    points+=p
                    valid.append(p)
                elif o=='+':
                    p=valid[len(valid)-2]+valid[len(valid)-1]
                    points+=p
                    valid.append(p)
        return points