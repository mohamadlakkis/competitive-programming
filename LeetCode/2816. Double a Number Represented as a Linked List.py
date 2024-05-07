#https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head):
            p=head.val*2
            if head.next:
                p+=helper(head.next)
            head.val=p%10
            k = p//10
            return k
        p=helper(head)
        if p:
            return ListNode(p,head)
        return head
