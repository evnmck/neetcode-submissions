class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        window_sum = 0
        max_frequency = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            window_size = right - left + 1
            cost = nums[right] * window_size - window_sum

            while cost > k:
                window_sum -= nums[left]
                left += 1

                window_size = right - left + 1
                cost = nums[right] * window_size - window_sum

            max_frequency = max(max_frequency, right - left + 1)

        return max_frequency