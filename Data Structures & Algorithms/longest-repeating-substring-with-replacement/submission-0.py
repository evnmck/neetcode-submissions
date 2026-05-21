class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        letters = {}

        for right in range(len(s)):
            letters[s[right]] = 1 + letters.get(s[right],0)
            
            while (right-left+1) - max(letters.values()) > k:
                letters[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)
        return longest


        