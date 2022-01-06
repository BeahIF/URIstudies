# To solve this problem, we are using the property of XOR.
# The result of XOR is 1 if the two bits are different.
# First XOR two numbers and then count number of 1s thats the answer.
# For counting set bits we are using Brian Kernighans Algorithm.
# Brian Kernighans algorithm every time performs a bitwise AND operation between n and n-1
# until n becomes zero. At each iteration increments the value of count variable.
#  Using this algo we only iterates the number of set bits times through the loop.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x^y
        i = 0
        while(xor>0):
            xor = xor & (xor-1)
            i=i+1
        return i
        