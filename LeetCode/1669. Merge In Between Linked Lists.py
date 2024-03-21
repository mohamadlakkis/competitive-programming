# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        count = 1
        while count<a:
            count+=1
            temp = temp.next
        temp2 = temp.next
        temp.next = list2
        i = 0
        BOUND = b-a+1
        while i<BOUND: ##### 
            temp2 = temp2.next
            i+=1
        while temp.next:
            temp = temp.next
        temp.next = temp2
        return list1
