class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sorted_piles = sorted(piles)

        left, right = 1, sorted_piles[-1]

        min_time = float('inf')

        while left <= right:
            mid = (left + right) // 2

            total_time = 0
            for i in sorted_piles:
                t = math.ceil(i / mid)
                total_time += t
                print(f"bananas: {i} // {mid} = {t}")
            
            print(f"Total time: {total_time} for k = {mid}")
            
            if total_time <= h:
                min_time = min(min_time, mid)
                right = mid - 1
            else:
                left = mid + 1
            
        
        return min_time