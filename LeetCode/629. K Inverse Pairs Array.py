#https://leetcode.com/problems/k-inverse-pairs-array/description/

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # A recursive solution, complexity(Time & Space) O(n**2 * k), doesn't work 
        # Key idea is that it doesn't matter of the numbers so we can keep track of the D efficiently !
        '''
        D = {}
        def X(i,t):
            if (i,t)in D:
                return D[(i,t)]
            if(t<=-1):return 0
            if (i==0):
                return 1 if t==0 else 0
            if(i==1 and t==1):return 0
            COUNT = 0
            for j in range(i):
                COUNT  = COUNT + X(i-1,t-j)
            D[(i,t)] = COUNT
            return COUNT
        return X(n,k)%(10**9 +7)
        '''
        #DP Solution 
        dp = [0]*(k+1)
        dp[0] = 1
        for N in range(1,n+1):
            temp = [0]*(k+1)
            total  = 0 
            for K in range(0,k+1):
                if K>=N:
                    total -=dp[K-N]
                total += dp[K]
                temp[K] = total
            dp = temp
        return dp[k]%(10**9 +7)