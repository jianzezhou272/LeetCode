class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size=size
        self.array=[]

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.array.append(val)
        if len(self.array)>self.size:
            self.array.pop(0)
        return sum(self.array)/float(len(self.array))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)