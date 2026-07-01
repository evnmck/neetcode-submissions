import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones

        heapq.heapify_max(heap)
        
        while len(heap) > 1:
            x, y = heapq.heappop_max(heap), heapq.heappop_max(heap)
            if x < y:
                heapq.heappush(heap, y - x)
            if y < x:
                heapq.heappush_max(heap, x - y)
  
        return heap[0] if len(heap) > 0 else 0
        