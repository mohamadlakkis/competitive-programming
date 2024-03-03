https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution(object):
    def removeNthFromEnd(self, head, n):

        # Create a dummy node to handle edge cases where the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer ahead by n+1 steps
        for i in range(n+1):
            first = first.next
        
        # Move both pointers simultaneously until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Now the second pointer points to the node just before the node to be deleted
        second.next = second.next.next
        
        return dummy.next
