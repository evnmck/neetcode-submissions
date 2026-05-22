class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_time = float('inf')

        while left <= right:
            mid = (left + right) // 2

            total_time = 0
            for i in piles:
                total_time += math.ceil(i / mid)
            
            if total_time <= h:
                min_time = min(min_time, mid)
                right = mid - 1
            else:
                left = mid + 1
            
        return min_time