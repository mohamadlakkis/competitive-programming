class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #Prefix_sum
       
        #O(n^2) this doesn't work, it will give us time limit exceeded 
        '''
        n = len(nums)
        #Here it is scalled by 1
        cum = [0]*(n+1)
        cum[1] = nums[0]
        for i in range(1,n):
            cum[i+1] = cum[i]+nums[i]
        COUNT = 0
        for i in range(1,n+1):
            for j in range(i,n+1):
                temp = cum[j]-cum[i-1]
                if temp==k:
                    COUNT+=1

        return COUNT
        '''
        #Solution that does actually work O(n) space and time
        cur = 0
        prefix = {0:1} #Key= sum, val = how many prefixes so far have sum = key
        COUNT = 0
        for n in nums:
            cur +=n
            diff  = cur-k
            if diff in prefix:
                COUNT += prefix[diff]
            prefix[cur] = 1+ prefix.get(cur,0)
        return COUNT
