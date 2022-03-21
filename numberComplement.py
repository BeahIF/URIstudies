#resolver usando xor
#5 é 101
#regra do xor = 00=0
#01=1
#10=1
#11=0
#5 xor com 1 = 101 ^ 001 = 100
#resultado xor com 2 =  100 ^ 010 =  110
#resultado xor com 4 = 110 ^ 100 = 010 -> que é o 
# complemento de 5 
#fazer o xor até o numero de entrada
#fazer o xor com x sendo x = 2^z z=(0,1,2,3.....)


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=1
        while(i<=num):
            
            num^=i
            i*=2
        return num