class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = (10**9)+7
        answer = 0
        nums.sort()

        for i in range(len(nums)):
            if nums[i] * 2 > target:
                break

            left, right = i, len(nums)-1
            temp_target = target - nums[i]

            while left < right:
                mid = left + (right - left + 1) // 2

                if nums[mid] <= temp_target:
                    left = mid
                else:
                    right = mid - 1
                     
            answer = (answer + pow(2, right - i, mod)) % mod

        return answer

