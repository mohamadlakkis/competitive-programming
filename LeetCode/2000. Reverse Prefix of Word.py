#https://leetcode.com/problems/reverse-prefix-of-word
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        target = 0
        for i,char in enumerate(list(word)):
            if char==ch:
                target= i
                break
        return word[0:target+1][::-1] + word[target+1:]
