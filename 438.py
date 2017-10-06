class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        mapp={}
        for lp in p:
            try:
                mapp[lp]+=1
            except:
                mapp[lp]=1
        maps={}
        l=len(p)
        for ls in s[:l]:
            try:
                maps[ls]+=1
            except:
                maps[ls]=1
        o=[]
        if maps==mapp:
            o.append(0)
        for i in range(1,len(s)-l+1):
            try:
                maps[s[i+l-1]]+=1
            except:
                maps[s[i+l-1]]=1
            if maps[s[i-1]]==1:
                del maps[s[i-1]]
            else:
                maps[s[i-1]]-=1
            if maps==mapp:
                o.append(i)
        return o