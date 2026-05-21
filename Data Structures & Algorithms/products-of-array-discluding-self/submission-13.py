from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        total = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total *= num

        output = []

        for num in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if num == 0:
                    output.append(total)
                else:
                    output.append(0)
            else:
                output.append(total // num)

        return output