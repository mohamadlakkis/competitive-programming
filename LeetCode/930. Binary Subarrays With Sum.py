#https://leetcode.com/problems/binary-subarrays-with-sum/
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

            #num of subarray les than or equl to goal -> helper(goal) - helper(goal-1)
            def helper(x):
                if x<0:return 0
                res = 0
                l = 0
                cur = 0
    
                for r in range(len(nums)):
                    cur +=nums[r]
                    while cur>x:
                        cur -=nums[l]
                        l+=1
                    res += (r-l+1)
                return res
            return helper(goal) -helper(goal-1)
