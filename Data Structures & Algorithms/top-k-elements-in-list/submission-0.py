class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = {}
        for num in nums:
            if num in results:
                results[num] += 1
            else:
                results[num] = 0
        
        bucket_list = [[] for i in range(len(nums))]
        
        for key, value in results.items():
            bucket_list[value].append(key)
        print(bucket_list)
        ret = []
        for y in range(len(bucket_list) - 1, -1, -1):
            numbers = bucket_list[y]
            print(numbers)
            if len(numbers) == 0:
                continue
            for z in numbers:
                ret.append(z)
            if len(ret) == k:
                return ret