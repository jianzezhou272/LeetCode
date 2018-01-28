class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        out = []
        dic = {}
        for l1 in 'QWERTYUIOP':
            dic[l1] = 1
        for l1 in 'ASDFGHJKL':
            dic[l1] = 2
        for l1 in 'ZXCVBNM':
            dic[l1] = 3

        for w in words:
            word = w.upper()
            for i in range(1, len(word)):
                if dic[word[i]] != dic[word[0]]:
                    break
            else:
                out.append(w)
        return out
