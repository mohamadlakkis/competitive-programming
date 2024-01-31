#https://leetcode.com/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        RES = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                T,IND = stack.pop()
                RES[IND] = (i-IND)
            stack.append([temp,i])
        return  RES
