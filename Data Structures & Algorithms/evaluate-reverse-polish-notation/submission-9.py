class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","/","*"}
        nums = []
    
        for token in tokens:
            if token in operators:
                b = nums.pop()
                a = nums.pop()
                ans = None
                if token == "+":
                    ans = a + b
                elif token == "-":
                    ans = a - b
                elif token == "/":
                    ans = int(a / b)
                elif token == "*":
                    ans = a * b
                nums.append(ans)
            else:
                nums.append(int(token))

        return nums[-1]

