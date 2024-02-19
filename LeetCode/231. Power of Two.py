#https://leetcode.com/problems/power-of-two/
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1))==0
    
    '''
    def isPowerOfTwo(self,n:int)->bool:
        return n>0 and (1<<30)%n==0
    '''
