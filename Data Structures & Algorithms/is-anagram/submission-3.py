class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.anotherAnswer(s, t)
        
    def original(self, s: str, t: str) -> bool:   
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

        for l in combination:
            if combination[l] != 0:
                return False
        return True

    def anotherAnswer(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = [0] * 26
        count_t = [0] * 26

        for x in range(len(s)):
            count_s[ord(s[x]) - ord('a')] += 1
            count_t[ord(t[x]) - ord('a')] += 1
        return count_s == count_t
        
