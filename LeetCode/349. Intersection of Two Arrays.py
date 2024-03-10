#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        D= {}
        d = {}
        for i in nums1:
            if i not in d:
                d[i]  = None
        for i in nums2:
            if i not in D and i in d:
                D[i]= None
        L = []
        for key in D:
            L.append(key)
        return L
