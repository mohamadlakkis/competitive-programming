#https://leetcode.com/problems/find-the-town-judge/description
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        D= {} #key = person, value  = list of people that trusts this person 
        D2 = {} #key = person, value = who this person trusts 
        if n ==1:return 1
        for a,b in trust:
            if b not in D:
                D[b] = 1
            else:
                D[b] +=1
            if a not in D2:
                D2[a] = None
            
        for key in D:
            if D[key]==n-1:
                if key not in D2:return key
        return -1
