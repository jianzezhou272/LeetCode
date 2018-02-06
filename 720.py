class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dic={}
        for w in words:
            dic[len(w)]=dic.get(len(w),[])+[w]
        l=min(dic.keys())
        while l+1 in dic.keys():
            l+=1
        for i in range(2,l+1):
            j=0
            while j<len(dic[i]):
                if dic[i][j][:-1] not in dic[i-1]:
                    dic[i].pop(j)
                else:
                    j+=1
        while not dic[l]:
            l-=1
        return sorted(dic[l])[0]