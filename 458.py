class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0

        else:
            rd = minutesToTest / minutesToDie + 1
            pig = 1
            while rd ** pig < buckets:
                pig += 1
            return pig