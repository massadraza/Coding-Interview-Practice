class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for x in s:
            if x == "{" or x == "[" or x == "(":
                stack.append(x)
            else:
                if not (not bool(stack)):
                    if stack.pop() != closeToOpen[x]:
                        return False
                else:
                    return False

        if not bool(stack):
            return True
        else:
            return False
