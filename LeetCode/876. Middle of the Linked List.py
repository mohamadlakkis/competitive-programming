#https://leetcode.com/problems/middle-of-the-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        count = 0
        
        while temp:
            count +=1
            temp  = temp.next
        n = 1+ count//2
        temp = head
        while n>1:
            n-=1
            temp = temp.next
        return temp
