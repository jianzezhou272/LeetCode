class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        o=[]
        for i in range(1,n+1):
            if i%3!=0 and i%5!=0:
                o.append(str(i))
            else:
                b3='Fizz' if i%3==0 else ''
                b5='Buzz' if i%5==0 else ''
                o.append(b3+b5)
        return o