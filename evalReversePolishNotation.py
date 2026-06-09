class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0

        for t in tokens: 
            if t != "+" and t != "-" and t != "/" and t != "*":
                stack.append(t)
            else:
                if t == "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif t == "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif t == "/":
                    secondNum = int(stack.pop())
                    firstNum = int(stack.pop())
                    stack.append(firstNum / secondNum)
                else:
                    secondNum = int(stack.pop())
                    firstNum = int(stack.pop())
                    stack.append(firstNum - secondNum)

        return int(stack.pop())
