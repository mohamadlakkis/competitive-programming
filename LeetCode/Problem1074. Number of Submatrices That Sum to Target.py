#https://leetcode.com/problems/number-of-submatrices-that-sum-to-target
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ## For the tutorial please check https://www.youtube.com/watch?v=43DRBP2DUHg (NeetCode's solution, very clever)
        # I didn't manage to solve this on my own, one of the hardest problems I have seen
        #I solve it but not efficiently for my code -> found at the end of this file
        ROWS,COLS = len(matrix),len(matrix[0])
        sub_sum = [[0]*(COLS+1) for i in range(ROWS+1)]
        #Remember in the sub_sum it is +1 since we addes he dimesnions by 1 so (M+1)by (N+1)
        #So in order to get the correct position of r,c in matrix we need to rescale them by -1 
        for r in range(1,ROWS+1):
            for c in range(1,COLS+1):
                sub_sum[r][c] = matrix[r-1][c-1]+sub_sum[r][c-1]+sub_sum[r-1][c]-sub_sum[r-1][c-1]
                
        COUNT = 0
        
        for r1 in range(1,ROWS+1):
            for r2 in range(r1,ROWS+1):
                count = defaultdict(int)
                count[0]=1
                for c in range(1,COLS+1):
                        cur = sub_sum[r2][c]-(sub_sum[r1-1][c] if r1>0 else 0)
                        diff = cur -target
                        COUNT += count[diff]
                        count[cur] += 1
        return COUNT
    '''
    class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS,COLS = len(matrix),len(matrix[0])
        sub_sum = [[0]*(COLS+1) for i in range(ROWS+1)]
        #Remember in the sub_sum it is +1 since we addes he dimesnions by 1 so (M+1)by (N+1)
        #So in order to get the correct position of r,c in matrix we need to rescale them by -1 
        for r in range(1,ROWS+1):
            for c in range(1,COLS+1):
                sub_sum[r][c] = matrix[r-1][c-1]+sub_sum[r][c-1]+sub_sum[r-1][c]-sub_sum[r-1][c-1]
                
        COUNT = 0
        
        for r1 in range(1,ROWS+1):
            for r2 in range(r1,ROWS+1):
                for c1 in range(1,COLS+1):
                    for c2 in range(c1,COLS+1):
                        temp = sub_sum[r2][c2]-sub_sum[r2][c1-1]-sub_sum[r1-1][c2]+sub_sum[r1-1][c1-1]
                        
                        if temp==target:
                            COUNT+=1
        return COUNT
                        
    '''
                        
