class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l=len(num)
        k=l/2
        if l%2==1 and num[k] not in '018':
            return False
        else:
            mir=''
            for i in range(1,k+1):
                if num[l-i] not in '01689':
                    return False
                elif num[l-i] in '69':
                    mir+=str(15-int(num[l-i]))
                else:
                    mir+=num[l-i]
            return mir==num[:k]