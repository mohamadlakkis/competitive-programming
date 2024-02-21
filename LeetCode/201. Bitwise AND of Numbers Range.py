#https://leetcode.com/problems/bitwise-and-of-numbers-range
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right>left:
            right &=(right-1)
        return right

    '''
    def rangeBitwiseAnd(left: int, right: int) -> int:
    L = [i for i in range(left,right+1)]
    n = len(L)
    res = 0
    BREAK = False
    COUNT = 0
    while not BREAK:
        ZERO = False
        for i in range(len(L)):
            if L[i]==0:
                BREAK = True
                
            if L[i]%2==0:
                ZERO = True
            L[i] = L[i]>>1
        if not ZERO:
            res += 2**i
        COUNT+=1
    return res

    ''' 
