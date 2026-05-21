class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for char in s1:
            s1_map[char] = 1 + s1_map.get(char,0)
        
        left = 0
        s2_map = {}

        for right in range(len(s2)):

            print(right)
            s2_map[s2[right]] = 1 + s2_map.get(s2[right],0)

            while s1_map.get(s2[right],0) - s2_map.get(s2[right],0) < 0:
                if s2[right] not in s1_map:
                    s2_map = {}
                    left = right + 1
                else:
                    s2_map[s2[left]] -= 1
                    left += 1
            
            if s1_map == s2_map:
                return True

        return s1_map == s2_map