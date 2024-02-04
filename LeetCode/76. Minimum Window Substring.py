#https://leetcode.com/problems/minimum-window-substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return ""

        T = {}
        for i in t:
            if i not in T:
                T[i] = 1
            else:
                T[i]+=1
        have = 0
        need = len(T)
        S = {}
        n = len(s)
        res,le = [-1,-1],float("inf")
        l = 0
        for i in range(n):
            c = s[i]
            S[c] = 1+S.get(c,0)
            
            if c in T and S[c]==T[c]:
                have +=1
            while have==need:
                if (i-l+1)<le:
                    res = [l,i]
                    le  = (i-l+1)
                S[s[l]] -=1
                if s[l] in T and S[s[l]]<T[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if le!=float("inf") else ""
                
                
