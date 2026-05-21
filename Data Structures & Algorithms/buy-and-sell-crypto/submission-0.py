class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        left, right = 0, 1 

        while right < len(prices):
            if prices[right] > prices[left]:
                maxProf = max(prices[right]-prices[left], maxProf)
            else:
                left = right
            right += 1

        return maxProf