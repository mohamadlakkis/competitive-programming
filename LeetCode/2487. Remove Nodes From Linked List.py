#https://leetcode.com/problems/remove-nodes-from-linked-list/submissions/1250635627/?envType=daily-question&envId=2024-05-06
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        prev_node = head
        current_node = head.next

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        head.next = None
        head = prev_node

        prev_node = head
        current_node = head.next
        while current_node:
            if current_node.val < prev_node.val:
                current_node = current_node.next
            else:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
        
        head.next = None
        head = prev_node
        return head
