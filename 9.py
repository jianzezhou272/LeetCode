class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x>=0 and int(str(x)[::-1])==x

#Another solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            tens=1
            while x/tens>9:
                tens*=10
            ini=x/tens
            tail=x%10
            while tens>=10:
                ini=x/tens
                tail=x%10
                if ini!=tail:
                    return False
                else:
                    x=(x-ini*tens)/10
                    tens/=100
            return True