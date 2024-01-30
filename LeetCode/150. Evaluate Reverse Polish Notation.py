#https://leetcode.com/problems/evaluate-reverse-polish-notation/description

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c== "+":
                a = stack.pop()
                n = stack.pop()
                stack.append(n+a)
            elif c== "-":
                a = stack.pop()
                n = stack.pop()
                stack.append(n-a)
            elif c=="/":
                a = stack.pop()
                n = stack.pop()
                stack.append(int(n/a))
            elif c=="*":
                a = stack.pop()
                n = stack.pop()
                stack.append(n*a)
            else:
                stack.append(int(c))
        return stack[0]
