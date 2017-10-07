class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        i = 0
        l = len(needle)
        L = len(haystack)
        while i + l <= L:
            if haystack[i:i + l] == needle:
                return i
            i += 1
        return -1