#https://leetcode.com/problems/largest-divisible-subset/description/
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        D = {}
        n = len(nums)
        nums.sort()
        def X(i):
            if i in D:
                return D[i]
            if i==n:return []
            MAX = [nums[i]]
            for j in range(i+1,n):
                if nums[j]%nums[i]==0:
                    L = [nums[i]] + X(j)
                    if len(L)>=len(MAX):
                        MAX = L
            
            D[i] = MAX
            return MAX
        MAX = []
        for i in range(n):
            P = X(i)
            if len(MAX)<len(P):
                MAX = P
        return MAX
