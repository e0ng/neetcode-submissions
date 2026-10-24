class MinStack:

    def __init__(self):
        self.stack = []
        self.help_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.help_stack :
            self.help_stack.append(val)
        else :
            if self.help_stack[-1]>=val:
                self.help_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.help_stack[-1]:
            self.help_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.help_stack[-1]

    # 스택 하나 더 만들기

