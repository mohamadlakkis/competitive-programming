#https://leetcode.com/problems/first-missing-positive/
#O(n) + O(n)
class Solution:
  #We can also use our input array as a memorey instead of using a dcitonary by using the fact that the number we are looking for is between 1 -> len(nums)+1, and using index of the arrays 
    def firstMissingPositive(self, nums: List[int]) -> int:
        D = {}
        for n in nums:
            if n not in D:
                D[n] = None
        for i in range(1,len(nums)+2):
            if i not in D:return i
        return -1
