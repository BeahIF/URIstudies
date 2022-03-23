class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # versao recursiva
        if(n==0):
            return 0
        if(n ==1):
            return 1 
        return fib(n-1)+fib(n-2)
        #versao sem recursao
        dp = [0 for x in range(N+1)]
        dp[0] = 0
        if N>=1:
            dp[1] = 1
            for x in range(2,N+1):
                dp[x] = dp[x-1]+dp[x-2]
        return dp[-1]