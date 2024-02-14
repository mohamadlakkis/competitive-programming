#https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        POS = deque()
        NEG = deque()
        n = len(nums)
        for i in nums:
            if i>0:POS.append(i)
            else:NEG.append(i)
        for i in range(n):
            if(i%2==0):nums[i] = POS.popleft()
            else:nums[i]=NEG.popleft()
        return nums

