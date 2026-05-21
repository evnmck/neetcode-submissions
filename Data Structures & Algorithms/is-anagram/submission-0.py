class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        combination = {}
        for c in range(len(s)):
            if s[c] not in combination:
                combination[s[c]] = 1
            else:
                combination[s[c]] = combination[s[c]] + 1
            if t[c] not in combination:
                combination[t[c]] = -1
            else:
                combination[t[c]] = combination[t[c]] - 1

        print(combination)
        for l in combination:
            if combination[l] != 0:
                return False
        return True