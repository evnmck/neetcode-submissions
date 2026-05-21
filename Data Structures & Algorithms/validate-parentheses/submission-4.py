class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if not stack:
                    return False
                compare = stack.pop()
                if char == ")" and compare != "(":
                    return False;
                elif char == "]" and compare != "[": 
                    return False;
                elif char == "}" and compare != "{":
                    return False;
        return len(stack) == 0