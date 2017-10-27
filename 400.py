class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur_dig=0
        while n>cur_dig*9*10**(cur_dig-1):
            n-=int(cur_dig*9*10**(cur_dig-1))
            cur_dig+=1
        start=int(10**(cur_dig-1)-1)
        if n%cur_dig==0:
            cur_num=start+n/cur_dig
            cur_bit=str(cur_num)[cur_dig-1]
            return int(cur_bit)
        else:
            cur_num=start+n/cur_dig+1
            cur_bit=str(cur_num)[n%cur_dig-1]
            return int(cur_bit)