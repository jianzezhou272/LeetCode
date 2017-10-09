class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        a = 0
        for c in s:
            if c == 'A':
                if a == 1:
                    return False
                else:
                    a += 1
                    l = 0
            elif c == 'P':
                l = 0
            elif c == 'L':
                if l <= 1:
                    l += 1
                else:
                    return False
        return True
