class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ms = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curmin = self.getMin()
        if curmin == None:
            curmin = x
        else:
            curmin = min(curmin, x)
        self.ms.append([x, curmin])

    def pop(self):
        """
        :rtype: void
        """
        self.ms.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.ms[len(self.ms) - 1][0]

    def getMin(self):
        """
        :rtype: int
        """
        try:
            return self.ms[len(self.ms) - 1][1]
        except:
            return None

            # Your MinStack object will be instantiated and called as such:
            # obj = MinStack()
            # obj.push(x)
            # obj.pop()
            # param_3 = obj.top()
            # param_4 = obj.getMin()