import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        heap = []
        queue = deque()
        time = 0

        for task in tasks:
            freqs[task] = freqs.get(task,0) + 1

        for task, freq in freqs.items():
            heapq.heappush_max(heap, (freq, task))

        while queue or heap:
            if not heap:
                time = queue[0][0]

            while queue and queue[0][0] <= time:
                avail, freq, task = queue.popleft()
                heapq.heappush_max(heap, (freq, task))
                
            freq, task = heapq.heappop_max(heap)
            freq -= 1

            if freq > 0:
                queue.append((time+n+1, freq, task))
                
            time += 1
        return time



        