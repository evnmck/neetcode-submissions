class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:

            mid = (left + right) // 2

            curr_days = 1
            cap = 0
            i = 0
            while i < len(weights):
                if cap + weights[i] <= mid:
                    cap += weights[i]
                else:
                    cap = weights[i]
                    curr_days += 1
                i += 1

            if curr_days <= days:
                right = mid
            else:
                left = mid + 1

        return left

        