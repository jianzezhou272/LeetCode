class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = set()
        self.pair = set()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """

        for n in list(self.num):
            if n + number not in self.pair:
                self.pair.add(n + number)
        if number not in self.num:
            self.num.add(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        return value in self.pair



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)
# too long

class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.num[number] = self.num.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.num:
            if n + n == value:
                if self.num[n] >= 2:
                    return True
            elif self.num.get(value - n):
                return True
        return False



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)