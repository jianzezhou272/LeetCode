class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n=len(words)
        for i in range(n):
            if len(words[i])>n:
                return False
            for j in range(i+1,n):
                print i,j
                if len(words[i])-1<j and len(words[j])-1>=i:
                    return False
                elif len(words[i])-1>=j and len(words[j])-1<i:
                    return False
                elif len(words[i])-1>=j and len(words[j])-1>=i and words[i][j]!=words[j][i]:
                    return False
        return True