class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        sev=''
        ab=abs(num)
        while ab>0:
            sev=str(ab%7)+sev
            ab/=7
        if num<0:
            sev='-'+sev
        if num==0:
            sev='0'
        return sev