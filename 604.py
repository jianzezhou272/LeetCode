class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.string = list(compressedString)
        self.curLetter = ' '
        self.curCount = 0

    def next(self):
        """
        :rtype: str
        """
        if self.curCount == 0:
            if len(self.string) > 0:
                self.curLetter = self.string.pop(0)
                self.curCount = ''
                while len(self.string) > 0 and self.string[0] in '1234567890':
                    self.curCount += self.string.pop(0)
            else:
                self.curCount = 1
                self.curLetter = ' '
        self.curCount = int(self.curCount)
        self.curCount -= 1
        return self.curLetter

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curCount > 0 or len(self.string) > 0


        # Your StringIterator object will be instantiated and called as such:
        # obj = StringIterator(compressedString)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()