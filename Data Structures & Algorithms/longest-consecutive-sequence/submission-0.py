class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            brute force 
              sort list and check sequence len w window
            
            optimal solution


        '''
        longestLen = 0
        cp = set(nums)

        for num in cp:
            currLen = 1
            if num-1 not in cp:
                while True:

                    if num+1 in cp:
                        num += 1
                        currLen += 1
                    else:
                        break
            longestLen = max(currLen, longestLen)
        

        return longestLen
