class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic_hex={
            0:'0',
            1:'1',
            2:'2',
            3:'3',
            4:'4',
            5:'5',
            6:'6',
            7:'7',
            8:'8',
            9:'9',
            10:'a',
            11:'b',
            12:'c',
            13:'d',
            14:'e',
            15:'f'
        }
        hx=''
        if num==0:
            return '0'
        else:
            if num<0:
                num+=2**32
            while num>0:
                hx=dic_hex[num%16]+hx
                num/=16
            return hx