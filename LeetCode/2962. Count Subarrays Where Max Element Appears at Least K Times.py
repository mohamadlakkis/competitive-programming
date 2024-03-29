#https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        MAX = max(nums)
        count = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if MAX==nums[r]:count+=1
            while count>=k and l<=r:
                if nums[l]==MAX:
                    count-=1
                l+=1
            res += r-l+1
        n = len(nums)
        return  n*(n+1)//2 - res
