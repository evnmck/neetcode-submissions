class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:

            mid = (left + right) // 2

            curr_days = 1
            cap = 0

            for weight in weights:
                if cap + weight <= mid:
                    cap += weight
                else:
                    cap = weight
                    curr_days += 1

            if curr_days <= days:
                right = mid
            else:
                left = mid + 1

        return left

        