class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = nums[0]
        output = [num for num in nums]
        numZero = 0
        for i in range(1,len(nums)):
            if nums[i] == 0:
                numZero += 1
                if numZero > 1:
                    total = 0 
                    break
            else:
                total = int(total * nums[i])

        for i in range(len(output)):
            if output[i] == 0:
                output[i] = total
            elif numZero == 1: 
                output[i] = 0
            else:
                output[i] = int(total / output[i])
        return output
        

        