#https://leetcode.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        
        dp=[n]*(n+1)
        dp[0] = 0
        for targ in range(1,n+1):   
            for s in range(1,targ+1):
                sq = s*s
                if sq>targ:
                    break
                dp[targ] = min(dp[targ],1+ dp[targ-sq])
        return dp[n]
