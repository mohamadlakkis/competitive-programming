#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        close_count = 0
        flag = 0
        ans = ""
        
        for char in s:
            if char == '(':
                open_count += 1
                flag += 1
            elif char == ')' and flag > 0:
                close_count += 1
                flag -= 1
        
        k = min(open_count, close_count)
        open_count = k
        close_count = k
        
        for char in s:
            if char == '(':
                if open_count > 0:
                    ans += '('
                    open_count -= 1
                continue
            if char == ')':
                if close_count > 0 and close_count > open_count:
                    ans += ')'
                    close_count -= 1
                continue
            else:
                ans += char
        
        return ans
