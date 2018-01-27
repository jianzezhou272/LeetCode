class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=bin(num)
        c='0b'
        for i in range(2,len(num)):
            c+=str(1-int(num[i]))
        return int(c,2)