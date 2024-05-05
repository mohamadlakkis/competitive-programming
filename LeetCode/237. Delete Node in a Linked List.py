#https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            return
        
        # Copy the value of the next node to the current node
        node.val = node.next.val
        
        # Skip the next node by updating the current node's next pointer
        node.next = node.next.next
