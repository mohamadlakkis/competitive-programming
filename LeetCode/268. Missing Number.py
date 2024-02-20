#https://leetcode.com/problems/missing-number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = n*(n+1)//2
        this = sum(nums)
        return abs(actual-this)
