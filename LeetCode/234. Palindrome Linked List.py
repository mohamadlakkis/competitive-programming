#https://leetcode.com/problems/palindrome-linked-list/description
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        
        l, r = 0, len(ans)-1

        while l < r and ans[l] == ans[r]:
            l += 1
            r -= 1 

        return l >= r 
