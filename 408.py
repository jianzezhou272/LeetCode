class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        word=list(word)
        abbr=list(abbr)
        curN=''
        for l in abbr:
            if l not in '1234567890':
                if len(curN)>0:
                    for i in range(int(curN)):
                        if len(word)==0:
                            return False
                        else:
                            word.pop(0)
                curN=''
                if len(word)==0 or l!=word[0]:
                    return False
                else:
                    word.pop(0)
            elif l=='0' and curN=='':
                return False
            else:
                curN+=l
        return (len(word)==0 and curN=='') or len(word)==int(curN)