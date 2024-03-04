#https://leetcode.com/problems/bag-of-tokens/
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        s = 0
        l = 0
        r = len(tokens)-1
        MAX = 0
        while l<=r:
            
            while l<=r and tokens[l]<=power:
                power-=tokens[l]
                l+=1
                s+=1
            MAX = max(MAX,s)
            if s>=1:
                power+=tokens[r]
                r-=1
                s-=1
            if (s<1 and l<=r and tokens[l]>power):break
        return MAX
            
