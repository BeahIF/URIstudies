class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res=0
        if(num<10):
            return num
        while(num>=10):
            res=0
            while(num>0):
                res = (num%10)+res
                num = num/10
            num=res
        return res