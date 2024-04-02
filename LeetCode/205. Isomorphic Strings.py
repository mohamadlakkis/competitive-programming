#https://leetcode.com/problems/isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        D = {}
        d = {}

        for charS, charT in zip(s, t):
            # If the character in s already has a mapping, check if it maps to the correct character in t
            if charS in D:
                if D[charS] != charT:
                    return False
            else:
                # If the character in t is already mapped to a different character in s, return false
                if charT in d:
                    return False
                D[charS] = charT
                d[charT] = charS

        return True
