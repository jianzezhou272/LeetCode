class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l = chars[0]
        n = 1
        i = 1
        while i < len(chars):
            if chars[i] == l:
                chars.pop(i)
                n += 1
            else:
                l = chars[i]
                if n > 1:
                    for d in str(n):
                        chars.insert(i, d)
                        i += 1
                i += 1
                n = 1
        print chars
        if n > 1:
            for d in str(n):
                chars += d
        return len(chars)
