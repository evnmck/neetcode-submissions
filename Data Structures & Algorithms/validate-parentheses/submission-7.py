class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                compare = stack.pop()
                if pairs[char] != compare:
                    return False
                     
        return len(stack) == 0