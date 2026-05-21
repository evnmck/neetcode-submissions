class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        i, j = 0, len(s)-1
        while i <= j:
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True