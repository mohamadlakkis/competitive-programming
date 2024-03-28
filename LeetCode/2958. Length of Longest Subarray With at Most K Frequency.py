#https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        D = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            D[nums[r]]+=1
            while D[nums[r]]>k:
                D[nums[l]]-=1
                l+=1
            res  = max(r-l+1,res)
        return res
