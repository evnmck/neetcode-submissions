class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        outerSeen = set()
        for i in range(len(nums)):
            k = 0 - nums[i]
            seen = set()
            for j in range(i+1,len(nums)):
                curr = nums[j]
                target = k - curr
                possible = sorted([nums[i],nums[j],target])
                if target in seen and (possible[0], possible[1], possible[2]) not in outerSeen:
                    ret.append(possible)
                    outerSeen.add((possible[0], possible[1], possible[2]))
                seen.add(curr)    
        return ret