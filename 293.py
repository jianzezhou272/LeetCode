class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        states=[]
        for i in range(len(s)-1):
            if s[i:i+2]=='++':
                states.append(s[0:i]+'--'+s[i+2:len(s)+1])
        return states