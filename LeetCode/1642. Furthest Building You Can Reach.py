#https://leetcode.com/problems/furthest-building-you-can-reach/
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''Max Heap solution ( we will be usig a min heap with negative #)'''
        heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff<=0:
                continue 
            bricks -=diff
            heapq.heappush(heap,-diff)
            if bricks <0:
                if ladders==0:
                    return i
                ladders-=1
                bricks += -heapq.heappop(heap)
        return len(heights)-1
        '''DP'''
        '''
        n = len(heights)
        
        def X(h,b,l):
            if(h==n-1):return 0
            if (heights[h]>=heights[h+1]):
                return 1+X(h+1,b,l)
            else:
                M = 0
                K = 0
                if(l!=0):
                    M = 1+X(h+1,b,l-1)
                temp = heights[h+1]-heights[h]
                if (temp<=b):
                    K = 1+X(h+1,b-temp,l)
                return max(M,K)
        return X(0,bricks,ladders)
        '''
