
class MinStack:

    def __init__(self):
        self.inner_stack = []
        self.min_value_stack = []

    def push(self, val: int) -> None:
        self.inner_stack.append(val)

        if not self.min_value_stack:
            self.min_value_stack.append(val)
        else:
            self.min_value_stack.append(min(self.min_value_stack[-1], val))

    def pop(self) -> None:
        self.inner_stack.pop()
        self.min_value_stack.pop()

    def top(self) -> int:
        return self.inner_stack[-1]

    def getMin(self) -> int:
        return self.min_value_stack[-1]
