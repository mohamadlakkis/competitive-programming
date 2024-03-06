#https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head 
        if not fast:return False
        fast = head.next
        slow = head
        while slow and fast: 
            if slow ==fast:return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return False
        return False
