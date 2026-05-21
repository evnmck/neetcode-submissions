class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        kv = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            if key not in kv:
                kv[key] = []
            
            kv[key].append(word)

        return list(kv.values())


