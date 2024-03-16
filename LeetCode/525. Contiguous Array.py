#https://leetcode.com/problems/contiguous-array/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_diff = 0  #C0 - C1
        max_length = 0 
        first_occurrence = {0:-1}
        for i, num in enumerate(nums):
            if num == 0:
                count_diff -= 1
            else:
                count_diff += 1
            if count_diff in first_occurrence:
                max_length = max(max_length, i - first_occurrence[count_diff])
            else:
                first_occurrence[count_diff] = i
        return max_length
