#https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        D = Counter(tasks)
        maxHeap = [-cnt for cnt in D.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #pairs 
        while maxHeap or q:
            time  +=1
            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt!=0:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])

        return time
                
                
