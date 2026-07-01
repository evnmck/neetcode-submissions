import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones

        heapq.heapify_max(heap)
        
        while len(heap) > 1:
            x, y = heapq.heappop_max(heap), heapq.heappop_max(heap)
            print(x,y,heap)
            if x < y:
                heapq.heappush_max(heap, y - x)
            if y < x:
                heapq.heappush_max(heap, x - y)
            print(heap)
  
        return heap[0] if len(heap) > 0 else 0
        