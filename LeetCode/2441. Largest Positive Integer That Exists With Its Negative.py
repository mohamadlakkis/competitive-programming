#https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        D = {}
        for i in nums:
            if i not in D:
                D[i] = None
        cur_max = -1
        for i in nums:
            if -i in D:
                if abs(i)>cur_max:
                    cur_max = abs(i)
        return cur_max
