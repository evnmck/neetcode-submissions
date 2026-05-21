class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_lists = []

        for word in strs:
            added = False
            for x in list_of_lists:
                if len(x) == 0:
                    x.append(word)
                    added = True
                else:
                    if self.isAnagram(x[0], word):
                        x.append(word)
                        added = True
            if not added:
                list_of_lists.append([word])
        return list_of_lists



    def isAnagram(self, word_one: str, word_two: str) -> bool:
        if len(word_one) != len(word_two):
            return False
        
        compare = {}
        for x in range(len(word_one)):
            char_one = word_one[x]
            char_two = word_two[x]
            if char_one not in compare:
                compare[char_one] = 1
            else:
                compare[char_one] = compare[char_one] + 1
            if char_two not in compare:
                compare[char_two] = -1
            else:
                compare[char_two] = compare[char_two] - 1
        for char, num in compare.items():
            if num != 0:
                return False

        return True
