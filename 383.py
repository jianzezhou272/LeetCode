class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r=list(set(ransomNote))
        for l in r:
            if ransomNote.count(l)>magazine.count(l):
                return False
        return True