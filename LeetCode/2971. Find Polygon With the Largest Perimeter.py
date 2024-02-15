class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        cum = 0
        i = 0
        #notice you can remove the cond of i>=2 since it will never happen 
        for n in nums:
            if cum>n and i>=2:
                res = cum+n
            cum+=n
            i+=1
        return res
