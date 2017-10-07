class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        else:
            count=self.countAndSay(n-1)
            say=''
            curn=count[0]
            curc=1
            for n in count[1:]:
                if n==curn:
                    curc+=1
                else:
                    say=say+str(curc)+curn
                    curn=n
                    curc=1
            say=say+str(curc)+curn
        return say