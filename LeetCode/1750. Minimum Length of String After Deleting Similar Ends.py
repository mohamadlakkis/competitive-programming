#https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description
class Solution:
    def minimumLength(self, s: str) -> int:
        #two pointers, left and right 
        l = 0
        r = len(s)-1
        REMOVED = 0
        while l<r:
            if s[l]!=s[r]:break
            if s[l]==s[r]:
                key = s[l]
                while l<r and s[l]==key:
                    l+=1
                    REMOVED +=1
                if l==r:
                    REMOVED+=1
                while l<r and s[r]==key:
                    r-=1
                    REMOVED +=1
        return len(s)-REMOVED
