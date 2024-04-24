#https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=2:
            if n==0:return 0
            return 1
        t_0 = 0
        t_1 = 1
        t_2 = 1
        cur =  0
        for i in range(2,n):
            cur = t_0+t_1+t_2
            temp_1 = t_1
            temp_2 = t_2
            t_0 = temp_1
            t_1 = temp_2
            t_2 = cur
        return cur
