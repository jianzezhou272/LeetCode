class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        for ls in s[::-1]:
            if ls not in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
                if l>0:
                    return l
            else:
                l+=1
        return l