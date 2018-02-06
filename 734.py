class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1)!=len(words2):
            return False
        else:
            prs={}
            for i in range(len(pairs)):
                prs[(pairs[i][0],pairs[i][1])]=True
                prs[(pairs[i][1],pairs[i][0])]=True
            for j in range(len(words1)):
                if words1[j]!=words2[j] and not prs.get((words1[j],words2[j])):
                    return False
            return True