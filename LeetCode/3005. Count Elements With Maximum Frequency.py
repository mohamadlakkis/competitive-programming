#https://leetcode.com/problems/count-elements-with-maximum-frequency
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        D = {}
        for i in nums:
            if i not in D:
                D[i] = 1
            else:
                D[i]+=1
        MAX = 0
        for key in D:
            MAX = max(MAX,D[key])
        COUNT = 0
        for key in D:
            if D[key]==MAX:COUNT+=MAX
        return COUNT
