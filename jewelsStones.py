class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count =0
        for i in jewels:
            if(i in stones):
            #tentativa que nao funciona no leetcode    
            # if(stones.index(i) >= 0):
                count =count+stones.count(i)
                
        return count