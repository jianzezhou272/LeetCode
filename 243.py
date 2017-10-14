class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1=None
        w2=None
        dis=sys.maxint
        for i in range(len(words)):
            if words[i]==word1:
                w1=i
                if w2!=None:
                    dis=min(dis,w1-w2)
            if words[i]==word2:
                w2=i
                if w1!=None:
                    dis=min(dis,w2-w1)
        return dis