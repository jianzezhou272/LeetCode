# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx=0
        while n>0:
            buf4=['']*4
            l=read4(buf4)
            if l==0:
                return idx
            else:
                a=min(l,n)
                buf[idx:idx+a]=buf4[0:a]
                idx+=a
                n-=a
        return idx