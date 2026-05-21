import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        topK = []

        for i in nums:
            if i in counts:
                counts[i] += 1 
            else:
                counts[i] = 1
        
        for key, val in counts.items():
            heapq.heappush(topK, (val, key))

            if len(topK) > k:
                heapq.heappop(topK)

        return [val for key, val in topK]