class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        alf='abcdefghijklmnopqrstuvwxyz'
        tg=alf.index(target)
        cur=tg+26
        out=''
        for l in letters:
            idx=alf.index(l)
            if idx<=tg:
                idx+=26
            if idx<cur:
                out=l
                cur=idx
        return out