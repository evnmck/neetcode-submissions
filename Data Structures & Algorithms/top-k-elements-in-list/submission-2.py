import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = {}
        for num in nums:
            if num in results:
                results[num] += 1
            else:
                results[num] = 1
        
        # bucket or heap
        heap = []

        for key, value in results.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
            
        return [val for count, val in heap]

    def bucket():
        bucket_list = [[] for i in range(len(nums)+1)]
        
        for key, value in results.items():
            bucket_list[value].append(key)
        ret = []
        for y in range(len(bucket_list) - 1, -1, -1):
            numbers = bucket_list[y]
            if len(numbers) == 0:
                continue
            for z in numbers:
                ret.append(z)
            if len(ret) >= k:
                return ret[:k]