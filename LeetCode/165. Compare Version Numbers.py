#https://leetcode.com/problems/compare-version-numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0 
        j = 0 
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        while i<len(ver1) and j<len(ver2):
            k1 = int(ver1[i])
            k2 = int(ver2[i])
            if k1<k2: return -1
            elif k2<k1:return 1
            i+=1
            j+=1
        if i==len(ver1) and j==len(ver2):return 0
        #check if ver1 rest are zeros
        while i<len(ver1):
            if int(ver1[i])!=0:return 1
            i+=1
        while j<len(ver2):
            if int(ver2[j])!=0:return -1
            j+=1
        return 0
        
