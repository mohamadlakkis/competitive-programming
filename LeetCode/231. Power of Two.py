#https://leetcode.com/problems/power-of-two/
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1))==0
