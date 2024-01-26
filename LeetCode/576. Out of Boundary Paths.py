#https://leetcode.com/problems/out-of-boundary-paths/
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        D = {}
        def X(i,j,count):
            if(i,j,count)in D:
                return D[(i,j,count)]
            if count > maxMove:
                return 0
            if i>=m or i<0 or j>=n or j<0:
                return 1
            D[(i,j,count)] = X(i+1,j,count+1)+X(i,j+1,count+1)+X(i,j-1,count+1)+X(i-1,j,count+1)
            return D[(i,j,count)]
        return X(startRow,startColumn,0)% (10**(9)+7)
    
