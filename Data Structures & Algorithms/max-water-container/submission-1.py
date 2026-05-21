class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            Brute force
                for every height in heights find the area for one other height
            optimal
                start at ends and whichever end is smaller move over
        '''

        left, right = 0, len(heights)-1 
        maxArea = 0
        while left < right:
            leftVal = heights[left]
            rightVal = heights[right]

            height = min(leftVal, rightVal)
            width = right - left

            maxArea = max(maxArea, width*height)
            
            if leftVal > rightVal:
                right -= 1
            else:
                left += 1
            
        return maxArea