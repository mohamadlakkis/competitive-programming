#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = s.split(" ")
        i = len(L)-1
        while i>=0 and L[i]=="":
            i-=1
        return len(L[i])
