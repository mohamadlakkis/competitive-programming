#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if not head:
            return head
        if not head.next:
            return head
        #actual code 
        behind = None
        front = head
        while front:
            temp = front.next
            front.next = behind
            behind = front
            front = temp
        return behind
