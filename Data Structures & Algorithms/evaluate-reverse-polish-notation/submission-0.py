class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()

                stack.append(self.cal(a, b, t))
            else:
                stack.append(int(t))

        return stack[-1]
    
    def cal(self, n1, n2, op):
        if op == "+":
            return n1+n2
        if op == "-":
            return n1-n2
        if op == "*":
            return n1*n2
        if op == "/":
            return int(n1/n2)
            
            