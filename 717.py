class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        elif len(bits) == 2:
            return bits[0] == 0
        elif len(bits) == 3:
            return bits[0] == 1 or bits[1] == 0 and bits[1] == 0
        else:
            string = []
            i = len(bits) - 2
            string = [bits[i] == 0]
            i -= 1
            string = [bits[i] == 1 or bits[i + 1] == 0 and bits[i] == 0] + string
            i -= 1
            while i >= 0:
                string = [bits[i] == 0 and string[0] or (bits[i] == 1 or bits[i + 1] == 0 and bits[i] == 0) and string[
                    1]] + string
                i -= 1
            return string[0]
