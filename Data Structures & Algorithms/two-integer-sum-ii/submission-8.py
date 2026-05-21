class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            indexSum = numbers[left] + numbers[right]

            if indexSum == target:
                return [left+1, right+1]
            
            if indexSum > target:
                right -= 1
            else:
                left += 1
        
