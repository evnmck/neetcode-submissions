from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        time = 0
        queue = deque()
        heap = []

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        for task in freq:
            heapq.heappush_max(heap, (freq[task], task))

        while queue or heap:

            if heap:
                count, task = heapq.heappop_max(heap)
                if count > 1:
                    queue.append((time+n, count-1, task))
            
            if queue and queue[0][0] == time:
                _, count, task = queue.popleft()
                heapq.heappush_max(heap, (count, task))

            time += 1
        
        return time


