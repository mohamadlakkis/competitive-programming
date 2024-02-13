#https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words: 
            i = 0
            j = len(w)-1
            while(i<=j and w[i]==w[j]):
                i+=1
                j-=1
            if(i>=j):return w

        return ""
