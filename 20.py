class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=[]
        for p in s:
            if p in '([{':
                left.append(p)
            elif p == ')':
                if len(left)==0 or left.pop()!='(':
                    return False
            elif p == ']':
                if len(left)==0 or left.pop()!='[':
                    return False
            elif p == '}':
                if len(left)==0 or left.pop()!='{':
                    return False
        return left==[]