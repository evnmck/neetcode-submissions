import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heap.append((dist, x, y))
        
        heapq.heapify(heap)

        ret = []

        while k > 0:
            dist, x , y = heapq.heappop(heap)

            ret.append([x,y])
            k -= 1

        return ret
        