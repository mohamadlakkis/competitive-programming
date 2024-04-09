#https://leetcode.com/problems/time-needed-to-buy-tickets/
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        curr = 0
        for i in range(len(tickets)):
            if i==k or i<=k:
                curr += min(tickets[k],tickets[i])
            else:
                curr += min(tickets[k]-1,tickets[i])
        return curr 
