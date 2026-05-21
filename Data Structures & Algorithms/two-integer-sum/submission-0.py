class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_index = {}
        for x in range(len(nums)):
            first = target - nums[x]
            if first in num_and_index:
                return [num_and_index[first], x]
            else: 
                num_and_index[nums[x]] = x