class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for char in s:
            if char in parentheses.keys():
                stack.append(parentheses[char])
            else:
                if stack:
                    if char == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return not stack
