#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_0 = 0 
        count_1 = 0
        for i in students: 
            if i ==0:count_0 +=1
            else: count_1+=1
        for i in sandwiches:
            if i==0 and count_0==0:return count_1
            if i==1 and count_1==0:return count_0
            if i==1: count_1-=1
            elif i==0:count_0-=1
        return 0
