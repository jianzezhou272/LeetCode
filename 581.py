class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack1 = [nums[0]]
        i = 1
        push = True
        while len(stack1) > 0 and i < len(nums):
            if nums[i] >= stack1[len(stack1) - 1]:
                if push:
                    stack1.append(nums[i])
            else:
                push = False
                while len(stack1) > 0 and nums[i] < stack1[len(stack1) - 1]:
                    stack1.pop()
            i += 1
        print stack1

        stack2 = [nums[len(nums) - 1]]
        i = len(nums) - 2
        push = True
        while len(stack2) > 0 and i >= 0:
            if nums[i] <= stack2[len(stack2) - 1]:
                if push:
                    stack2.append(nums[i])
            else:
                push = False
                while len(stack2) > 0 and nums[i] > stack2[len(stack2) - 1]:
                    stack2.pop()
            i -= 1
        return max(len(nums) - len(stack1) - len(stack2), 0)