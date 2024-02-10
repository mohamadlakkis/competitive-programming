#https://leetcode.com/problems/palindromic-substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        COUNT = 0
        for i in range(len(s)):
            #Odd Case
            l,r = i,i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                COUNT +=1
                l-=1
                r+=1
            #Even Case
            
            l,r = i-1,i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                COUNT+=1
                l-=1
                r+=1
        return COUNT
